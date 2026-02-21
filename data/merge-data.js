// 데이터 통합 스크립트
const fs = require('fs');
const path = require('path');

console.log('=== SomeThing 데이터 통합 시작 ===\n');

// 파일 목록
const files = [
  'questions-10gen.json',
  'questions-priority.json',
  'questions-20late.json',
  'questions-30gen.json',
  'questions-missing.json'
];

const allCombinations = {};
let totalCombinations = 0;
let totalQuestions = 0;

// 각 파일 로드 및 병합
files.forEach(file => {
  const filePath = path.join(__dirname, file);
  
  if (!fs.existsSync(filePath)) {
    console.log(`❌ 파일 없음: ${file}`);
    return;
  }
  
  try {
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const key = Object.keys(data)[0]; // 첫 번째 키로 데이터 구조 확인
    
    let combinations = {};
    
    // 파일 구조 확인
    if (data.combinations) {
      // priority 파일은 "combinations" 필드에 있음
      combinations = data.combinations;
    } else {
      // 나머지 파일은 최상위에 조합이 있음
      combinations = data;
    }
    
    // 각 조합 병합
    Object.keys(combinations).forEach(key => {
      if (allCombinations[key]) {
        console.log(`⚠️ 중복 키 발견: ${key} (덮어쓰기)`);
      }
      allCombinations[key] = combinations[key];
      totalCombinations++;
      
      // 질문 수 계산
      ['sum', 'self', 'other'].forEach(test => {
        if (combinations[key][test] && Array.isArray(combinations[key][test])) {
          totalQuestions += combinations[key][test].length;
        }
      });
    });
    
    console.log(`✅ 로드 완료: ${file} (${Object.keys(combinations).length}개 조합)`);
  } catch (err) {
    console.log(`❌ 오류: ${file} - ${err.message}`);
  }
});

// 최종 통합 데이터 생성
const finalData = {
  metadata: {
    version: "2.0",
    created: "2026-02-21",
    combinations: totalCombinations,
    tests_per_combination: 3,
    total_question_sets: totalCombinations * 3,
    total_questions: totalQuestions
  },
  combinations: allCombinations
};

// 저장
const outputPath = path.join(__dirname, 'questions-full.json');
fs.writeFileSync(outputPath, JSON.stringify(finalData, null, 2), 'utf8');

console.log('\n=== 통합 완료 ===');
console.log(`📁 저장 파일: questions-full.json`);
console.log(`📊 총 조합: ${totalCombinations}개`);
console.log(`📝 총 문항: ${totalQuestions}개`);
console.log(`💾 파일 크기: ${(fs.statSync(outputPath).size / 1024).toFixed(1)}KB`);
