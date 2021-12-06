data "local_file" "input" {
    filename = "input"
}

locals {
    commands = split("\n", data.local_file.input.content)
    steps   = [ for step in local.commands : split(" ", step) ]
    forward = [ for step in local.steps : tonumber(step[1]) if step[0] == "forward" ]
    down    = [ for step in local.steps : tonumber(step[1]) if step[0] == "down" ]
    up      = [ for step in local.steps : tonumber(step[1]) if step[0] == "up" ]
    aim_changes = [
        for step in local.steps :
            (step[0] == "up" ? 1 : (step[0] == "down" ? -1 : 0)) * tonumber(step[1])
    ]
    aim_values = [
        for i, aim in local.aim_changes : 
            i == 0 ? 0 : sum(slice(local.aim_changes, 0, i))
    ]
    depths = [
        for i, step in local.steps :
            local.aim_values[i] * tonumber(step[1]) if step[0] == "forward"
    ]
}

output "part1" {
    value = abs(sum(local.forward) * (sum(local.up) - sum(local.down)))
}
output "part2" {
    value = sum(local.forward) * abs(sum(local.depths))
}