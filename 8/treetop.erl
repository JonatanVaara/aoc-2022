-module(treetop)
-compile(export_all)


main(Inputfile) ->
    


create_list_from_file(Inputfile) ->
    case file:read_file(Inputfile) of
        {ok, Output} ->
            turn_to_list(Output);
        {error, Reason} ->
            io:format("~p", [Reason])
    end.
