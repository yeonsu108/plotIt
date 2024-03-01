#pragma once
#include <string>

class CommandLineCfg {

    public:
        static CommandLineCfg& get() {
            static CommandLineCfg instance;
            return instance;
        }

        bool ignore_scales = false;
        bool verbose = false;
        bool do_plots = true;
        bool do_yields = false;
        bool do_systematics = false;
        bool do_qcd = false;
        bool unblind = false;
        bool systematicsBreakdown = false;
        bool dyincl = false;
        bool desytop = false;
        bool allSig = false;
        bool binned = false;
        std::string era = "";

    private:
        CommandLineCfg() = default;

};
