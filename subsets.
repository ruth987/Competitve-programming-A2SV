class Solution {
public:
    void solve(vector<int> &tmp,vector<vector<int>> &ans,int s,vector<int> &nums){
        ans.push_back(tmp);
        if(s==nums.size()){
            return;
        }
        
        for(int i = s; i < nums.size(); i++){
            tmp.push_back(nums[i]);
            solve(tmp,ans,i+1,nums);
            tmp.pop_back();
            while(i+1<nums.size() && nums[s] == nums[i+1]){
                i++;
            }
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> tmp;
        solve(tmp,ans,0,nums);
        return ans;
    }
};