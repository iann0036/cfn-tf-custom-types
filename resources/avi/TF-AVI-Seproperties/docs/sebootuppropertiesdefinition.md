# TF::AVI::Seproperties SeBootupPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dockerbackendportend" title="DockerBackendPortend">DockerBackendPortend</a>" : <i>Double</i>,
    "<a href="#dockerbackendportstart" title="DockerBackendPortstart">DockerBackendPortstart</a>" : <i>Double</i>,
    "<a href="#fairqueueingenabled" title="FairQueueingEnabled">FairQueueingEnabled</a>" : <i>Boolean</i>,
    "<a href="#geodbgranularity" title="GeoDbGranularity">GeoDbGranularity</a>" : <i>Double</i>,
    "<a href="#l7connspercore" title="L7ConnsPerCore">L7ConnsPerCore</a>" : <i>Double</i>,
    "<a href="#l7resvdlistenconnspercore" title="L7ResvdListenConnsPerCore">L7ResvdListenConnsPerCore</a>" : <i>Double</i>,
    "<a href="#logagentdebugenabled" title="LogAgentDebugEnabled">LogAgentDebugEnabled</a>" : <i>Boolean</i>,
    "<a href="#logagenttraceenabled" title="LogAgentTraceEnabled">LogAgentTraceEnabled</a>" : <i>Boolean</i>,
    "<a href="#seemulatedcores" title="SeEmulatedCores">SeEmulatedCores</a>" : <i>Double</i>,
    "<a href="#seipencapipc" title="SeIpEncapIpc">SeIpEncapIpc</a>" : <i>Double</i>,
    "<a href="#sel3encapipc" title="SeL3EncapIpc">SeL3EncapIpc</a>" : <i>Double</i>,
    "<a href="#selogbufferappblockingdequeue" title="SeLogBufferAppBlockingDequeue">SeLogBufferAppBlockingDequeue</a>" : <i>Boolean</i>,
    "<a href="#selogbufferapplogsize" title="SeLogBufferApplogSize">SeLogBufferApplogSize</a>" : <i>Double</i>,
    "<a href="#selogbufferchunkcount" title="SeLogBufferChunkCount">SeLogBufferChunkCount</a>" : <i>Double</i>,
    "<a href="#selogbufferconnblockingdequeue" title="SeLogBufferConnBlockingDequeue">SeLogBufferConnBlockingDequeue</a>" : <i>Boolean</i>,
    "<a href="#selogbufferconnlogsize" title="SeLogBufferConnlogSize">SeLogBufferConnlogSize</a>" : <i>Double</i>,
    "<a href="#selogbuffereventsblockingdequeue" title="SeLogBufferEventsBlockingDequeue">SeLogBufferEventsBlockingDequeue</a>" : <i>Boolean</i>,
    "<a href="#selogbuffereventssize" title="SeLogBufferEventsSize">SeLogBufferEventsSize</a>" : <i>Double</i>,
    "<a href="#sslsesscachepervs" title="SslSessCachePerVs">SslSessCachePerVs</a>" : <i>Double</i>,
    "<a href="#sslsesscachetimeout" title="SslSessCacheTimeout">SslSessCacheTimeout</a>" : <i>Double</i>,
    "<a href="#tcpsyncachehashsize" title="TcpSyncacheHashsize">TcpSyncacheHashsize</a>" : <i>Double</i>,
    "<a href="#sedpcompression" title="SeDpCompression">SeDpCompression</a>" : <i>[ <a href="sedpcompressiondefinition.md">SeDpCompressionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dockerbackendportend" title="DockerBackendPortend">DockerBackendPortend</a>: <i>Double</i>
<a href="#dockerbackendportstart" title="DockerBackendPortstart">DockerBackendPortstart</a>: <i>Double</i>
<a href="#fairqueueingenabled" title="FairQueueingEnabled">FairQueueingEnabled</a>: <i>Boolean</i>
<a href="#geodbgranularity" title="GeoDbGranularity">GeoDbGranularity</a>: <i>Double</i>
<a href="#l7connspercore" title="L7ConnsPerCore">L7ConnsPerCore</a>: <i>Double</i>
<a href="#l7resvdlistenconnspercore" title="L7ResvdListenConnsPerCore">L7ResvdListenConnsPerCore</a>: <i>Double</i>
<a href="#logagentdebugenabled" title="LogAgentDebugEnabled">LogAgentDebugEnabled</a>: <i>Boolean</i>
<a href="#logagenttraceenabled" title="LogAgentTraceEnabled">LogAgentTraceEnabled</a>: <i>Boolean</i>
<a href="#seemulatedcores" title="SeEmulatedCores">SeEmulatedCores</a>: <i>Double</i>
<a href="#seipencapipc" title="SeIpEncapIpc">SeIpEncapIpc</a>: <i>Double</i>
<a href="#sel3encapipc" title="SeL3EncapIpc">SeL3EncapIpc</a>: <i>Double</i>
<a href="#selogbufferappblockingdequeue" title="SeLogBufferAppBlockingDequeue">SeLogBufferAppBlockingDequeue</a>: <i>Boolean</i>
<a href="#selogbufferapplogsize" title="SeLogBufferApplogSize">SeLogBufferApplogSize</a>: <i>Double</i>
<a href="#selogbufferchunkcount" title="SeLogBufferChunkCount">SeLogBufferChunkCount</a>: <i>Double</i>
<a href="#selogbufferconnblockingdequeue" title="SeLogBufferConnBlockingDequeue">SeLogBufferConnBlockingDequeue</a>: <i>Boolean</i>
<a href="#selogbufferconnlogsize" title="SeLogBufferConnlogSize">SeLogBufferConnlogSize</a>: <i>Double</i>
<a href="#selogbuffereventsblockingdequeue" title="SeLogBufferEventsBlockingDequeue">SeLogBufferEventsBlockingDequeue</a>: <i>Boolean</i>
<a href="#selogbuffereventssize" title="SeLogBufferEventsSize">SeLogBufferEventsSize</a>: <i>Double</i>
<a href="#sslsesscachepervs" title="SslSessCachePerVs">SslSessCachePerVs</a>: <i>Double</i>
<a href="#sslsesscachetimeout" title="SslSessCacheTimeout">SslSessCacheTimeout</a>: <i>Double</i>
<a href="#tcpsyncachehashsize" title="TcpSyncacheHashsize">TcpSyncacheHashsize</a>: <i>Double</i>
<a href="#sedpcompression" title="SeDpCompression">SeDpCompression</a>: <i>
      - <a href="sedpcompressiondefinition.md">SeDpCompressionDefinition</a></i>
</pre>

## Properties

#### DockerBackendPortend

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerBackendPortstart

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FairQueueingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoDbGranularity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L7ConnsPerCore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L7ResvdListenConnsPerCore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentDebugEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAgentTraceEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeEmulatedCores

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeIpEncapIpc

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeL3EncapIpc

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogBufferAppBlockingDequeue

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogBufferApplogSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogBufferChunkCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogBufferConnBlockingDequeue

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogBufferConnlogSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogBufferEventsBlockingDequeue

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLogBufferEventsSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSessCachePerVs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSessCacheTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSyncacheHashsize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDpCompression

_Required_: No

_Type_: List of <a href="sedpcompressiondefinition.md">SeDpCompressionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

