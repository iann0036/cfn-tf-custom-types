# TF::AzureRM::AppService SiteConfigDefinition

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDocuments

The ordering of default documents to load, if an address isn't specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DotnetFrameworkVersion

The version of the .net framework's CLR used in this App Service. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`), `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`) and `v5.0`. [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpsState

State of FTP / FTPS service for this App Service. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

The health check path to be pinged by App Service. [For more information - please see App Service health check announcement](https://azure.github.io/AppService/2020/08/24/healthcheck-on-app-service.html).

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

The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JAVA`, `JETTY`, and `TOMCAT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaContainerVersion

The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaVersion

The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11` and their specific versions - except for Java 11 (e.g. `1.7.0_80`, `1.8.0_181`, `11`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxFxVersion

Linux App Framework and version for the App Service. Possible options are a Docker container (`DOCKER|<user/image:tag>`), a base-64 encoded Docker Compose file (`COMPOSE|${filebase64("compose.yml")}`) or a base-64 encoded Kubernetes Manifest (`KUBE|${filebase64("kubernetes.yml")}`).

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

The scaled number of workers (for per site scaling) of this App Service. Requires that `per_site_scaling` is enabled on the `azurerm_app_service_plan`. [For more information - please see Microsoft documentation on high-density hosting](https://docs.microsoft.com/en-us/azure/app-service/manage-scale-per-app).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhpVersion

The version of PHP to use in this App Service. Possible values are `5.5`, `5.6`, `7.0`, `7.1`, `7.2`, `7.3` and `7.4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PythonVersion

The version of Python to use in this App Service. Possible values are `2.7` and `3.4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDebuggingEnabled

Is Remote Debugging Enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDebuggingVersion

Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmIpRestriction

A [List of objects](/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.

_Required_: No

_Type_: List of <a href="scmiprestrictiondefinition2.md">ScmIpRestrictionDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmType

The type of Source Control enabled for this App Service. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO`, and `VSTSRM`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmUseMainIpRestriction

IP security restrictions for scm to use main. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Use32BitWorkerProcess

Should the App Service run in 32 bit mode, rather than 64 bit mode?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsocketsEnabled

Should WebSockets be enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsFxVersion

The Windows Docker container image (`DOCKER|<user/image:tag>`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="corsdefinition.md">CorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

