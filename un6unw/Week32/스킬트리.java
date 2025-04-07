class Solution {
    public int solution(String skill, String[] skill_trees) {
        int validCount = 0;

        for (String tree : skill_trees) {
            StringBuilder filtered = new StringBuilder();

            // 스킬트리에서 선행 스킬만 골라냄
            for (char c : tree.toCharArray()) {
                if (skill.indexOf(c) != -1) {
                    filtered.append(c);
                }
            }

            // skill의 접두사(prefix)인지 확인
            if (skill.startsWith(filtered.toString())) {
                validCount++;
            }
        }

        return validCount;
    }
}