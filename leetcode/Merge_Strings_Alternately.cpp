class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        auto itW1 = word1.begin();
        auto itW2 = word2.begin();
        while (true){
            if(itW1 != word1.end()){
                result.push_back(*itW1); 
                ++itW1;
            }else{
                for(;itW2 !=word2.end(); ++itW2){
                    result.push_back(*itW2);
                }
                break;
            }
            if(itW2!=word2.end()){
                result.push_back(*itW2);
                ++itW2;
            }else{
                for(;itW1!=word1.end(); ++itW1){
                    result.push_back(*itW1);
                }
                break;
            }
        }
        return result;
    }
};