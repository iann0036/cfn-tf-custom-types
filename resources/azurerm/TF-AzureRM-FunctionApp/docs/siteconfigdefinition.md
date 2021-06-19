# TF::AzureRM::FunctionApp SiteConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwayson" title="AlwaysOn">AlwaysOn</a>" : <i>Boolean</i>,
    "<a href="#autoswapslotname" title="AutoSwapSlotName">AutoSwapSlotName</a>" : <i>String</i>,
    "<a href="#ftpsstate" title="FtpsState">FtpsState</a>" : <i>String</i>,
    "<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>" : <i>String</i>,
    "<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>" : <i>Boolean</i>,
    "<a href="#iprestriction" title="IpRestriction">IpRestriction</a>" : <i>[ <a href="iprestrictiondefinition2.md">IpRestrictionDefinition2</a>, ... ]</i>,
    "<a href="#javaversion" title="JavaVersion">JavaVersion</a>" : <i>String</i>,
    "<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>" : <i>String</i>,
    "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
    "<a href="#prewarmedinstancecount" title="PreWarmedInstanceCount">PreWarmedInstanceCount</a>" : <i>Double</i>,
    "<a href="#scmiprestriction" title="ScmIpRestriction">ScmIpRestriction</a>" : <i>[ <a href="scmiprestrictiondefinition2.md">ScmIpRestrictionDefinition2</a>, ... ]</i>,
    "<a href="#scmtype" title="ScmType">ScmType</a>" : <i>String</i>,
    "<a href="#scmusemainiprestriction" title="ScmUseMainIpRestriction">ScmUseMainIpRestriction</a>" : <i>Boolean</i>,
    "<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>" : <i>Boolean</i>,
    "<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>" : <i>Boolean</i>,
    "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="corsdefinition.md">CorsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwayson" title="AlwaysOn">AlwaysOn</a>: <i>Boolean</i>
<a href="#autoswapslotname" title="AutoSwapSlotName">AutoSwapSlotName</a>: <i>String</i>
<a href="#ftpsstate" title="FtpsState">FtpsState</a>: <i>String</i>
<a href="#healthcheckpath" title="HealthCheckPath">HealthCheckPath</a>: <i>String</i>
<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>: <i>Boolean</i>
<a href="#iprestriction" title="IpRestriction">IpRestriction</a>: <i>
      - <a href="iprestrictiondefinition2.md">IpRestrictionDefinition2</a></i>
<a href="#javaversion" title="JavaVersion">JavaVersion</a>: <i>String</i>
<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>: <i>String</i>
<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
<a href="#prewarmedinstancecount" title="PreWarmedInstanceCount">PreWarmedInstanceCount</a>: <i>Double</i>
<a href="#scmiprestriction" title="ScmIpRestriction">ScmIpRestriction</a>: <i>
      - <a href="scmiprestrictiondefinition2.md">ScmIpRestrictionDefinition2</a></i>
<a href="#scmtype" title="ScmType">ScmType</a>: <i>String</i>
<a href="#scmusemainiprestriction" title="ScmUseMainIpRestriction">ScmUseMainIpRestriction</a>: <i>Boolean</i>
<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>: <i>Boolean</i>
<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>: <i>Boolean</i>
<a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="corsdefinition.md">CorsDefinition</a></i>
</pre>

## Properties

#### AlwaysOn

Should the Function App be loaded at all times? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSwapSlotName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpsState

State of FTP / FTPS service for this function app. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`. Defaults to `AllAllowed`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPath

Path which will be checked for this function app health.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Enabled

Specifies whether or not the http2 protocol should be enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRestriction

A [List of objects](/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.

_Required_: No

_Type_: List of <a href="iprestrictiondefinition2.md">IpRestrictionDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaVersion

Java version hosted by the function app in Azure. Possible values are `1.8`, `11`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxFxVersion

Linux App Framework and version for the AppService, e.g. `DOCKER|(golang:latest)`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

The minimum supported TLS version for the function app. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new function apps.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreWarmedInstanceCount

The number of pre-warmed instances for this function app. Only affects apps on the Premium plan.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmIpRestriction

A [List of objects](/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.

_Required_: No

_Type_: List of <a href="scmiprestrictiondefinition2.md">ScmIpRestrictionDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmType

The type of Source Control used by the Function App. Valid values include: `BitBucketGit`, `BitBucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None` (default), `OneDrive`, `Tfs`, `VSO`, and `VSTSRM`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScmUseMainIpRestriction

IP security restrictions for scm to use main. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Use32BitWorkerProcess

Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsocketsEnabled

Should WebSockets be enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="corsdefinition.md">CorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

