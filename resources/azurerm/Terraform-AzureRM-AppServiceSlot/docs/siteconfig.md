# Terraform::AzureRM::AppServiceSlot SiteConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwayson" title="AlwaysOn">AlwaysOn</a>" : <i>Boolean</i>,
    "<a href="#appcommandline" title="AppCommandLine">AppCommandLine</a>" : <i>String</i>,
    "<a href="#autoswapslotname" title="AutoSwapSlotName">AutoSwapSlotName</a>" : <i>String</i>,
    "<a href="#defaultdocuments" title="DefaultDocuments">DefaultDocuments</a>" : <i>[ String, ... ]</i>,
    "<a href="#dotnetframeworkversion" title="DotnetFrameworkVersion">DotnetFrameworkVersion</a>" : <i>String</i>,
    "<a href="#ftpsstate" title="FtpsState">FtpsState</a>" : <i>String</i>,
    "<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>" : <i>Boolean</i>,
    "<a href="#iprestriction" title="IpRestriction">IpRestriction</a>" : <i>[ <a href="siteconfig-iprestriction.md">IpRestriction</a>, ... ]</i>,
    "<a href="#javacontainer" title="JavaContainer">JavaContainer</a>" : <i>String</i>,
    "<a href="#javacontainerversion" title="JavaContainerVersion">JavaContainerVersion</a>" : <i>String</i>,
    "<a href="#javaversion" title="JavaVersion">JavaVersion</a>" : <i>String</i>,
    "<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>" : <i>String</i>,
    "<a href="#localmysqlenabled" title="LocalMysqlEnabled">LocalMysqlEnabled</a>" : <i>Boolean</i>,
    "<a href="#managedpipelinemode" title="ManagedPipelineMode">ManagedPipelineMode</a>" : <i>String</i>,
    "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
    "<a href="#phpversion" title="PhpVersion">PhpVersion</a>" : <i>String</i>,
    "<a href="#pythonversion" title="PythonVersion">PythonVersion</a>" : <i>String</i>,
    "<a href="#remotedebuggingenabled" title="RemoteDebuggingEnabled">RemoteDebuggingEnabled</a>" : <i>Boolean</i>,
    "<a href="#remotedebuggingversion" title="RemoteDebuggingVersion">RemoteDebuggingVersion</a>" : <i>String</i>,
    "<a href="#scmtype" title="ScmType">ScmType</a>" : <i>String</i>,
    "<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>" : <i>Boolean</i>,
    "<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>" : <i>Boolean</i>,
    "<a href="#windowsfxversion" title="WindowsFxVersion">WindowsFxVersion</a>" : <i>String</i>,
    "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="siteconfig-cors.md">Cors</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwayson" title="AlwaysOn">AlwaysOn</a>: <i>Boolean</i>
<a href="#appcommandline" title="AppCommandLine">AppCommandLine</a>: <i>String</i>
<a href="#autoswapslotname" title="AutoSwapSlotName">AutoSwapSlotName</a>: <i>String</i>
<a href="#defaultdocuments" title="DefaultDocuments">DefaultDocuments</a>: <i>
      - String</i>
<a href="#dotnetframeworkversion" title="DotnetFrameworkVersion">DotnetFrameworkVersion</a>: <i>String</i>
<a href="#ftpsstate" title="FtpsState">FtpsState</a>: <i>String</i>
<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>: <i>Boolean</i>
<a href="#iprestriction" title="IpRestriction">IpRestriction</a>: <i>
      - <a href="siteconfig-iprestriction.md">IpRestriction</a></i>
<a href="#javacontainer" title="JavaContainer">JavaContainer</a>: <i>String</i>
<a href="#javacontainerversion" title="JavaContainerVersion">JavaContainerVersion</a>: <i>String</i>
<a href="#javaversion" title="JavaVersion">JavaVersion</a>: <i>String</i>
<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>: <i>String</i>
<a href="#localmysqlenabled" title="LocalMysqlEnabled">LocalMysqlEnabled</a>: <i>Boolean</i>
<a href="#managedpipelinemode" title="ManagedPipelineMode">ManagedPipelineMode</a>: <i>String</i>
<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
<a href="#phpversion" title="PhpVersion">PhpVersion</a>: <i>String</i>
<a href="#pythonversion" title="PythonVersion">PythonVersion</a>: <i>String</i>
<a href="#remotedebuggingenabled" title="RemoteDebuggingEnabled">RemoteDebuggingEnabled</a>: <i>Boolean</i>
<a href="#remotedebuggingversion" title="RemoteDebuggingVersion">RemoteDebuggingVersion</a>: <i>String</i>
<a href="#scmtype" title="ScmType">ScmType</a>: <i>String</i>
<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>: <i>Boolean</i>
<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>: <i>Boolean</i>
<a href="#windowsfxversion" title="WindowsFxVersion">WindowsFxVersion</a>: <i>String</i>
<a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="siteconfig-cors.md">Cors</a></i>
</pre>

## Properties

#### AlwaysOn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCommandLine

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSwapSlotName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDocuments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DotnetFrameworkVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpsState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRestriction

_Required_: No

_Type_: List of <a href="siteconfig-iprestriction.md">IpRestriction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaContainerVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxFxVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalMysqlEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedPipelineMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhpVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PythonVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDebuggingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDebuggingVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Use32BitWorkerProcess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsocketsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsFxVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="siteconfig-cors.md">Cors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

