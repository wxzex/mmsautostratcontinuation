loadstring(game:HttpGet("https://raw.githubusercontent.com/wxzex/mmsautostratcontinuation/main/justincase/sjkdkjlfdjnnmklcvxjNotifCr"))()

if not getgenv().OtherCOAV2 then
    getgenv().OtherCOAV2 = true
    say("SCRIPT", "Made by Money Maker")
    local breaks = false
    local cc = 0
    local Commanders = {}
    local chainStatus = ""
    local rmF = game:GetService("ReplicatedStorage").RemoteFunction
    local lib = loadstring(game:HttpGet("https://raw.githubusercontent.com/wxzex/mmsautostratcontinuation/main/libcode", true))()
    local w = lib:CreateWindow("Auto Chain V2")
    w:Section("Status :")
    w:Section("ChainStatus")
    local cs = nil

    for i, v in pairs(game.CoreGui:GetDescendants()) do
        if v:IsA("TextLabel") and v.Text == "ChainStatus" then
            cs = v
        end
    end

    spawn(function()
        while wait() do
            cs.Text = chainStatus
        end
    end)

    function getTroopTypeCheck(troop)
        return troop.Replicator:GetAttribute("Type")
    end

    function getTroopType(tr)
        local check = getTroopTypeCheck(tr)
        if check then
            return check
        else
            return "Unable to GET"
        end
    end

    function getNextClickedTroop()
        local Mouse = game.Players.LocalPlayer:GetMouse()
        local _Tower = nil
        local con
        con = Mouse.Button1Down:Connect(function()
            for i, v in pairs(game.Workspace.Towers:GetChildren()) do
                if v.Owner.Value == game.Players.LocalPlayer.UserId and v:IsAncestorOf(Mouse.Target) and getTroopType(v) == "Commander" and v ~= Commanders[1] and v ~= Commanders[2] and v ~= Commanders[3] then
                    _Tower = v
                    con:Disconnect()
                    break
                end
            end
        end)
        repeat wait() until _Tower
        return _Tower
    end

    for c = 1, 3 do
        chainStatus = "Click On Commander " .. tostring(c)
        table.insert(Commanders, getNextClickedTroop())
    end

    repeat wait() until Commanders[3] ~= nil

    getgenv().Coms = Commanders

    function Act(Comm)
        local Towers = game:GetService("Workspace").Towers
        if Commanders[Comm] ~= nil then
            local Tower = Commanders[Comm]
            if not Tower.Replicator.Stuns:GetAttribute("1") and not Tower.Replicator.Stuns:GetAttribute("2") and not Tower.Replicator.Stuns:GetAttribute("3") then
                rmF:InvokeServer("Troops", "Abilities", "Activate", {["Troop"] = Tower, ["Name"] = "Call Of Arms", ["AutoChain"] = true})
            else
                chainStatus = "Stun on commander " .. tostring(Comm)
                repeat wait() until not Tower.Replicator.Stuns:GetAttribute("1") and not Tower.Replicator.Stuns:GetAttribute("2") and not Tower.Replicator.Stuns:GetAttribute("3")
                rmF:InvokeServer("Troops", "Abilities", "Activate", {["Troop"] = Tower, ["Name"] = "Call Of Arms", ["AutoChain"] = true})
            end
        else
            chainStatus = "Commander " .. tostring(Comm) .. " removed"
            breaks = true
        end
    end

    getgenv().OtherCOAV2 = false

    while wait() do
        if breaks then
            break
        end
        Act(1)
        chainStatus = "Chaining Commander 1"
        wait(10.01)
        Act(2)
        chainStatus = "Chaining Commander 2"
        wait(10.01)
        Act(3)
        chainStatus = "Chaining Commander 3"
        wait(10.01)
    end

    breaks = false
else
    say("ERROR", "Looks like other coa is setting up commanders at the moment!")
end
