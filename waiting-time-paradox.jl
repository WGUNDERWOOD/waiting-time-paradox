using Random

#n = 100
start_time = 600
average_interval = 10
#interarrival_times = 10 * randexp(Float64, n)
#arrival_times = cumsum(interarrival_times)
#waiting_time = max.(arrival_times .- start_time, 0)

#println(waiting_time .>= 0)
#println(trunc.(Int, arrival_times))

function get_waiting_time_info(average_interval, start_time)

    arrival_time = 0
    old_arrival_time = 0

    while arrival_time - start_time < 0

        interval = average_interval * randexp(Float64)
        old_arrival_time = arrival_time
        arrival_time += interval
    end

    waiting_time = arrival_time - start_time
    elapsed_time = start_time - old_arrival_time
    observed_interval = arrival_time - old_arrival_time

    waiting_time_info = Dict(
        "waiting_time" => waiting_time,
        "elapsed_time" => elapsed_time,
        "observed_interval" => observed_interval
    )

    return waiting_time_info
end

waiting_time = get_waiting_time_info(average_interval, start_time)
println(waiting_time)
