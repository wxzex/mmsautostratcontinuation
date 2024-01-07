loadstring(game:HttpGet("https://raw.githubusercontent.com/wxzex/mmsautostratcontinuation/main/justincase/sjkdkjlfdjnnmklcvxjNotifCr"))()
say("SCRIPT", "Made by Money Maker")
getgenv().breaks = false
local cc = 0
getgenv().Commanders = {}
getgenv().RecorderSync = false
local rmF = game:GetService("ReplicatedStorage").RemoteFunction

for i, v in pairs(game:GetService("Workspace").Towers:GetChildren()) do
    if cc <= 3 then
        if v:FindFirstChild("Owner") then
            if v.Owner.Value == game.Players.LocalPlayer.UserId and v.Replicator:GetAttribute("Type") == "Commander" then
                table.insert(getgenv().Commanders, v)
            end
        end
    else
        break
    end
end

for c = 1, 3 do
    if getgenv().Commanders[c] ~= nil and getgenv().Commanders[c]:FindFirstChild("Owner").Value == game.Players.LocalPlayer.UserId then
        say("WARNING", "Commander" .. tostring(c) .. " detected")
    else
        say("WARNING", "Commander " .. tostring(c) .. " not placed, waiting to be placed...")
        local conn
        conn = game:GetService("Workspace").Towers.ChildAdded:Connect(function(v)
            if v:WaitForChild("Owner") then
                if v.Owner.Value == game.Players.LocalPlayer.UserId and v.Replicator:GetAttribute("Type") == "Commander" then
                    table.insert(getgenv().Commanders, v)
                end
            end
        end)

        repeat
            wait()
        until getgenv().Commanders[c] ~= nil

        conn:Disconnect()
    end
end

function Act(Comm)
    local Towers = game:GetService("Workspace").Towers
    if getgenv().Commanders[Comm] ~= nil then
        local Tower = getgenv().Commanders[Comm]
        if not Tower.Replicator.Stuns:GetAttribute("1") and not Tower.Replicator.Stuns:GetAttribute("2") and not Tower.Replicator.Stuns:GetAttribute("3") then
            rmF:InvokeServer("Troops", "Abilities", "Activate", {["Troop"] = Tower, ["Name"] = "Call Of Arms", ["AutoChain"] = true})
        else
            say("WARNING", "Detected stun on commander " .. tostring(Comm) .. ", waiting...")
            repeat
                wait()
            until not Tower.Replicator.Stuns:GetAttribute("1") and not Tower.Replicator.Stuns:GetAttribute("2") and not Tower.Replicator.Stuns:GetAttribute("3")
            rmF:InvokeServer("Troops", "Abilities", "Activate", {["Troop"] = Tower, ["Name"] = "Call Of Arms", ["AutoChain"] = true})
        end
    else
        say("ERROR", "Commander " .. tostring(Comm) .. " removed, aborting script...")
        getgenv().breaks = true
    end
end

say("WARNING", "AutoChain activated")
getgenv().RecorderSync = true

while wait() do
    if getgenv().breaks then
        break
    end
    Act(1)
    wait(10.01)
    Act(2)
    wait(10.01)
    Act(3)
    wait(10.01)
end

getgenv().breaks = false
