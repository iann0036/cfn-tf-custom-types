# TF::AzureRM::KubernetesCluster SysctlConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fsaiomaxnr" title="FsAioMaxNr">FsAioMaxNr</a>" : <i>Double</i>,
    "<a href="#fsfilemax" title="FsFileMax">FsFileMax</a>" : <i>Double</i>,
    "<a href="#fsinotifymaxuserwatches" title="FsInotifyMaxUserWatches">FsInotifyMaxUserWatches</a>" : <i>Double</i>,
    "<a href="#fsnropen" title="FsNrOpen">FsNrOpen</a>" : <i>Double</i>,
    "<a href="#kernelthreadsmax" title="KernelThreadsMax">KernelThreadsMax</a>" : <i>Double</i>,
    "<a href="#netcorenetdevmaxbacklog" title="NetCoreNetdevMaxBacklog">NetCoreNetdevMaxBacklog</a>" : <i>Double</i>,
    "<a href="#netcoreoptmemmax" title="NetCoreOptmemMax">NetCoreOptmemMax</a>" : <i>Double</i>,
    "<a href="#netcorermemdefault" title="NetCoreRmemDefault">NetCoreRmemDefault</a>" : <i>Double</i>,
    "<a href="#netcorermemmax" title="NetCoreRmemMax">NetCoreRmemMax</a>" : <i>Double</i>,
    "<a href="#netcoresomaxconn" title="NetCoreSomaxconn">NetCoreSomaxconn</a>" : <i>Double</i>,
    "<a href="#netcorewmemdefault" title="NetCoreWmemDefault">NetCoreWmemDefault</a>" : <i>Double</i>,
    "<a href="#netcorewmemmax" title="NetCoreWmemMax">NetCoreWmemMax</a>" : <i>Double</i>,
    "<a href="#netipv4iplocalportrangemax" title="NetIpv4IpLocalPortRangeMax">NetIpv4IpLocalPortRangeMax</a>" : <i>Double</i>,
    "<a href="#netipv4iplocalportrangemin" title="NetIpv4IpLocalPortRangeMin">NetIpv4IpLocalPortRangeMin</a>" : <i>Double</i>,
    "<a href="#netipv4neighdefaultgcthresh1" title="NetIpv4NeighDefaultGcThresh1">NetIpv4NeighDefaultGcThresh1</a>" : <i>Double</i>,
    "<a href="#netipv4neighdefaultgcthresh2" title="NetIpv4NeighDefaultGcThresh2">NetIpv4NeighDefaultGcThresh2</a>" : <i>Double</i>,
    "<a href="#netipv4neighdefaultgcthresh3" title="NetIpv4NeighDefaultGcThresh3">NetIpv4NeighDefaultGcThresh3</a>" : <i>Double</i>,
    "<a href="#netipv4tcpfintimeout" title="NetIpv4TcpFinTimeout">NetIpv4TcpFinTimeout</a>" : <i>Double</i>,
    "<a href="#netipv4tcpkeepaliveintvl" title="NetIpv4TcpKeepaliveIntvl">NetIpv4TcpKeepaliveIntvl</a>" : <i>Double</i>,
    "<a href="#netipv4tcpkeepaliveprobes" title="NetIpv4TcpKeepaliveProbes">NetIpv4TcpKeepaliveProbes</a>" : <i>Double</i>,
    "<a href="#netipv4tcpkeepalivetime" title="NetIpv4TcpKeepaliveTime">NetIpv4TcpKeepaliveTime</a>" : <i>Double</i>,
    "<a href="#netipv4tcpmaxsynbacklog" title="NetIpv4TcpMaxSynBacklog">NetIpv4TcpMaxSynBacklog</a>" : <i>Double</i>,
    "<a href="#netipv4tcpmaxtwbuckets" title="NetIpv4TcpMaxTwBuckets">NetIpv4TcpMaxTwBuckets</a>" : <i>Double</i>,
    "<a href="#netipv4tcptwreuse" title="NetIpv4TcpTwReuse">NetIpv4TcpTwReuse</a>" : <i>Boolean</i>,
    "<a href="#netnetfilternfconntrackbuckets" title="NetNetfilterNfConntrackBuckets">NetNetfilterNfConntrackBuckets</a>" : <i>Double</i>,
    "<a href="#netnetfilternfconntrackmax" title="NetNetfilterNfConntrackMax">NetNetfilterNfConntrackMax</a>" : <i>Double</i>,
    "<a href="#vmmaxmapcount" title="VmMaxMapCount">VmMaxMapCount</a>" : <i>Double</i>,
    "<a href="#vmswappiness" title="VmSwappiness">VmSwappiness</a>" : <i>Double</i>,
    "<a href="#vmvfscachepressure" title="VmVfsCachePressure">VmVfsCachePressure</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#fsaiomaxnr" title="FsAioMaxNr">FsAioMaxNr</a>: <i>Double</i>
<a href="#fsfilemax" title="FsFileMax">FsFileMax</a>: <i>Double</i>
<a href="#fsinotifymaxuserwatches" title="FsInotifyMaxUserWatches">FsInotifyMaxUserWatches</a>: <i>Double</i>
<a href="#fsnropen" title="FsNrOpen">FsNrOpen</a>: <i>Double</i>
<a href="#kernelthreadsmax" title="KernelThreadsMax">KernelThreadsMax</a>: <i>Double</i>
<a href="#netcorenetdevmaxbacklog" title="NetCoreNetdevMaxBacklog">NetCoreNetdevMaxBacklog</a>: <i>Double</i>
<a href="#netcoreoptmemmax" title="NetCoreOptmemMax">NetCoreOptmemMax</a>: <i>Double</i>
<a href="#netcorermemdefault" title="NetCoreRmemDefault">NetCoreRmemDefault</a>: <i>Double</i>
<a href="#netcorermemmax" title="NetCoreRmemMax">NetCoreRmemMax</a>: <i>Double</i>
<a href="#netcoresomaxconn" title="NetCoreSomaxconn">NetCoreSomaxconn</a>: <i>Double</i>
<a href="#netcorewmemdefault" title="NetCoreWmemDefault">NetCoreWmemDefault</a>: <i>Double</i>
<a href="#netcorewmemmax" title="NetCoreWmemMax">NetCoreWmemMax</a>: <i>Double</i>
<a href="#netipv4iplocalportrangemax" title="NetIpv4IpLocalPortRangeMax">NetIpv4IpLocalPortRangeMax</a>: <i>Double</i>
<a href="#netipv4iplocalportrangemin" title="NetIpv4IpLocalPortRangeMin">NetIpv4IpLocalPortRangeMin</a>: <i>Double</i>
<a href="#netipv4neighdefaultgcthresh1" title="NetIpv4NeighDefaultGcThresh1">NetIpv4NeighDefaultGcThresh1</a>: <i>Double</i>
<a href="#netipv4neighdefaultgcthresh2" title="NetIpv4NeighDefaultGcThresh2">NetIpv4NeighDefaultGcThresh2</a>: <i>Double</i>
<a href="#netipv4neighdefaultgcthresh3" title="NetIpv4NeighDefaultGcThresh3">NetIpv4NeighDefaultGcThresh3</a>: <i>Double</i>
<a href="#netipv4tcpfintimeout" title="NetIpv4TcpFinTimeout">NetIpv4TcpFinTimeout</a>: <i>Double</i>
<a href="#netipv4tcpkeepaliveintvl" title="NetIpv4TcpKeepaliveIntvl">NetIpv4TcpKeepaliveIntvl</a>: <i>Double</i>
<a href="#netipv4tcpkeepaliveprobes" title="NetIpv4TcpKeepaliveProbes">NetIpv4TcpKeepaliveProbes</a>: <i>Double</i>
<a href="#netipv4tcpkeepalivetime" title="NetIpv4TcpKeepaliveTime">NetIpv4TcpKeepaliveTime</a>: <i>Double</i>
<a href="#netipv4tcpmaxsynbacklog" title="NetIpv4TcpMaxSynBacklog">NetIpv4TcpMaxSynBacklog</a>: <i>Double</i>
<a href="#netipv4tcpmaxtwbuckets" title="NetIpv4TcpMaxTwBuckets">NetIpv4TcpMaxTwBuckets</a>: <i>Double</i>
<a href="#netipv4tcptwreuse" title="NetIpv4TcpTwReuse">NetIpv4TcpTwReuse</a>: <i>Boolean</i>
<a href="#netnetfilternfconntrackbuckets" title="NetNetfilterNfConntrackBuckets">NetNetfilterNfConntrackBuckets</a>: <i>Double</i>
<a href="#netnetfilternfconntrackmax" title="NetNetfilterNfConntrackMax">NetNetfilterNfConntrackMax</a>: <i>Double</i>
<a href="#vmmaxmapcount" title="VmMaxMapCount">VmMaxMapCount</a>: <i>Double</i>
<a href="#vmswappiness" title="VmSwappiness">VmSwappiness</a>: <i>Double</i>
<a href="#vmvfscachepressure" title="VmVfsCachePressure">VmVfsCachePressure</a>: <i>Double</i>
</pre>

## Properties

#### FsAioMaxNr

The sysctl setting fs.aio-max-nr. Must be between `65536` and `6553500`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsFileMax

The sysctl setting fs.file-max. Must be between `8192` and `12000500`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsInotifyMaxUserWatches

The sysctl setting fs.inotify.max_user_watches. Must be between `781250` and `2097152`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsNrOpen

The sysctl setting fs.nr_open. Must be between `8192` and `20000500`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelThreadsMax

The sysctl setting kernel.threads-max. Must be between `20` and `513785`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetCoreNetdevMaxBacklog

The sysctl setting net.core.netdev_max_backlog. Must be between `1000` and `3240000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetCoreOptmemMax

The sysctl setting net.core.optmem_max. Must be between `20480` and `4194304`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetCoreRmemDefault

The sysctl setting net.core.rmem_default. Must be between `212992` and `134217728`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetCoreRmemMax

The sysctl setting net.core.rmem_max. Must be between `212992` and `134217728`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetCoreSomaxconn

The sysctl setting net.core.somaxconn. Must be between `4096` and `3240000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetCoreWmemDefault

The sysctl setting net.core.wmem_default. Must be between `212992` and `134217728`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetCoreWmemMax

The sysctl setting net.core.wmem_max. Must be between `212992` and `134217728`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4IpLocalPortRangeMax

The sysctl setting net.ipv4.ip_local_port_range max value. Must be between `1024` and `60999`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4IpLocalPortRangeMin

The sysctl setting net.ipv4.ip_local_port_range min value. Must be between `1024` and `60999`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4NeighDefaultGcThresh1

The sysctl setting net.ipv4.neigh.default.gc_thresh1. Must be between `128` and `80000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4NeighDefaultGcThresh2

The sysctl setting net.ipv4.neigh.default.gc_thresh2. Must be between `512` and `90000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4NeighDefaultGcThresh3

The sysctl setting net.ipv4.neigh.default.gc_thresh3. Must be between `1024` and `100000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4TcpFinTimeout

The sysctl setting net.ipv4.tcp_fin_timeout. Must be between `5` and `120`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4TcpKeepaliveIntvl

The sysctl setting net.ipv4.tcp_keepalive_intvl. Must be between `10` and `75`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4TcpKeepaliveProbes

The sysctl setting net.ipv4.tcp_keepalive_probes. Must be between `1` and `15`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4TcpKeepaliveTime

The sysctl setting net.ipv4.tcp_keepalive_time. Must be between `30` and `432000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4TcpMaxSynBacklog

The sysctl setting net.ipv4.tcp_max_syn_backlog. Must be between `128` and `3240000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4TcpMaxTwBuckets

The sysctl setting net.ipv4.tcp_max_tw_buckets. Must be between `8000` and `1440000`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetIpv4TcpTwReuse

The sysctl setting net.ipv4.tcp_tw_reuse. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetNetfilterNfConntrackBuckets

The sysctl setting net.netfilter.nf_conntrack_buckets. Must be between `65536` and `147456`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetNetfilterNfConntrackMax

The sysctl setting net.netfilter.nf_conntrack_max. Must be between `131072` and `589824`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmMaxMapCount

The sysctl setting vm.max_map_count. Must be between `65530` and `262144`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSwappiness

The sysctl setting vm.swappiness. Must be between `0` and `100`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmVfsCachePressure

The sysctl setting vm.vfs_cache_pressure. Must be between `0` and `100`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

