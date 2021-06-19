# TF::AzureRM::AppServiceSlot SiteConfigDefinition

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
    "<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>" : <i>String</i>,
    "<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>" : <i>Boolean</i>,
    "<a href="#iprestriction" title="IpRestriction">IpRestriction</a>" : <i>[ <a href="iprestrictiondefinition2.md">IpRestrictionDefinition2</a>, ... ]</i>,
    "<a href="#javacontainer" title="JavaContainer">JavaContainer</a>" : <i>String</i>,
    "<a href="#javacontainerversion" title="JavaContainerVersion">JavaContainerVersion</a>" : <i>String</i>,
    "<a href="#javaversion" title="JavaVersion">JavaVersion</a>" : <i>String</i>,
    "<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>" : <i>String</i>,
    "<a href="#localmysqlenabled" title="LocalMysqlEnabled">LocalMysqlEnabled</a>" : <i>Boolean</i>,
    "<a href="#managedpipelinemode" title="ManagedPipelineMode">ManagedPipelineMode</a>" : <i>String</i>,
    "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
    "<a href="#numberofworkers" title="NumberOfWorkers">NumberOfWorkers</a>" : <i>Double</i>,
    "<a href="#phpversion" title="PhpVersion">PhpVersion</a>" : <i>String</i>,
    "<a href="#pythonversion" title="PythonVersion">PythonVersion</a>" : <i>String</i>,
    "<a href="#remotedebuggingenabled" title="RemoteDebuggingEnabled">RemoteDebuggingEnabled</a>" : <i>Boolean</i>,
    "<a href="#remotedebuggingversion" title="RemoteDebuggingVersion">RemoteDebuggingVersion</a>" : <i>String</i>,
    "<a href="#scmiprestriction" title="ScmIpRestriction">ScmIpRestriction</a>" : <i>[ <a href="scmiprestrictiondefinition2.md">ScmIpRestrictionDefinition2</a>, ... ]</i>,
    "<a href="#scmtype" title="ScmType">ScmType</a>" : <i>String</i>,
    "<a href="#scmusemainiprestriction" title="ScmUseMainIpRestriction">ScmUseMainIpRestriction</a>" : <i>Boolean</i>,
    "<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>" : <i>Boolean</i>,
    "<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>" : <i>Boolean</i>,
    "<a href="#windowsfxversion" title="WindowsFxVersion">WindowsFxVersion</a>" : <i>String</i>,
    "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="corsdefinition.md">CorsDefinition</a>, ... ]</i>
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
<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>: <i>String</i>
<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>: <i>Boolean</i>
<a href="#iprestriction" title="IpRestriction">IpRestriction</a>: <i>
      - <a href="iprestrictiondefinition2.md">IpRestrictionDefinition2</a></i>
<a href="#javacontainer" title="JavaContainer">JavaContainer</a>: <i>String</i>
<a href="#javacontainerversion" title="JavaContainerVersion">JavaContainerVersion</a>: <i>String</i>
<a href="#javaversion" title="JavaVersion">JavaVersion</a>: <i>String</i>
<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>: <i>String</i>
<a href="#localmysqlenabled" title="LocalMysqlEnabled">LocalMysqlEnabled</a>: <i>Boolean</i>
<a href="#managedpipelinemode" title="ManagedPipelineMode">ManagedPipelineMode</a>: <i>String</i>
<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
<a href="#numberofworkers" title="NumberOfWorkers">NumberOfWorkers</a>: <i>Double</i>
<a href="#phpversion" title="PhpVersion">PhpVersion</a>: <i>String</i>
<a href="#pythonversion" title="PythonVersion">PythonVersion</a>: <i>String</i>
<a href="#remotedebuggingenabled" title="RemoteDebuggingEnabled">RemoteDebuggingEnabled</a>: <i>Boolean</i>
<a href="#remotedebuggingversion" title="RemoteDebuggingVersion">RemoteDebuggingVersion</a>: <i>String</i>
<a href="#scmiprestriction" title="ScmIpRestriction">ScmIpRestriction</a>: <i>
      - <a href="scmiprestrictiondefinition2.md">ScmIpRestrictionDefinition2</a></i>
<a href="#scmtype" title="ScmType">ScmType</a>: <i>String</i>
<a href="#scmusemainiprestriction" title="ScmUseMainIpRestriction">ScmUseMainIpRestriction</a>: <i>Boolean</i>
<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>: <i>Boolean</i>
<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>: <i>Boolean</i>
<a href="#windowsfxversion" title="WindowsFxVersion">WindowsFxVersion</a>: <i>String</i>
<a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="corsdefinition.md">CorsDefinition</a></i>
</pre>

## Properties

#### AlwaysOn

Should the app be loaded at all times? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCommandLine

App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSwapSlotName

The name of the slot to automatically swap to during deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDocuments

The ordering of default documents to load, if an address isn't specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DotnetFrameworkVersion

The version of the .net framework's CLR used in this App Service Slot. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpsState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Enabled

Is HTTP2 Enabled on this App Service? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRestriction

A [List of objects](/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.

_Required_: No

_Type_: List of <a href="iprestrictiondefinition2.md">IpRestrictionDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaContainer

The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JETTY` and `TOMCAT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaContainerVersion

The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaVersion

The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8`, and `11` and their specific versions - except for Java 11 (e.g. `1.7.0_80`, `1.8.0_181`, `11`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxFxVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalMysqlEnabled

Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedPipelineMode

The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfWorkers

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhpVersion

The version of PHP to use in this App Service Slot. Possible values are `5.5`, `5.6`, `7.0`, `7.1`, `7.2`, and `7.3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PythonVersion

The version of Python to use in this App Service Slot. Possible values are `2.7` and `3.4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDebuggingEnabled

Is Remote Debugging Enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDebuggingVersion

Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015`, and `VS2017`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmIpRestriction

_Required_: No

_Type_: List of <a href="scmiprestrictiondefinition2.md">ScmIpRestrictionDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmType

The type of Source Control enabled for this App Service Slot. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO`, and `VSTSRM`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmUseMainIpRestriction

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Use32BitWorkerProcess

Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsocketsEnabled

Should WebSockets be enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsFxVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="corsdefinition.md">CorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

