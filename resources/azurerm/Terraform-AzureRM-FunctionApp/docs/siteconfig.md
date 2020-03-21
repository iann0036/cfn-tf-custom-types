# Terraform::AzureRM::FunctionApp SiteConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwayson" title="AlwaysOn">AlwaysOn</a>" : <i>Boolean</i>,
    "<a href="#ftpsstate" title="FtpsState">FtpsState</a>" : <i>String</i>,
    "<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>" : <i>Boolean</i>,
    "<a href="#iprestriction" title="IpRestriction">IpRestriction</a>" : <i>[ <a href="siteconfig-iprestriction.md">IpRestriction</a>, ... ]</i>,
    "<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>" : <i>String</i>,
    "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
    "<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>" : <i>Boolean</i>,
    "<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>" : <i>Boolean</i>,
    "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="siteconfig-cors.md">Cors</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwayson" title="AlwaysOn">AlwaysOn</a>: <i>Boolean</i>
<a href="#ftpsstate" title="FtpsState">FtpsState</a>: <i>String</i>
<a href="#http2enabled" title="Http2Enabled">Http2Enabled</a>: <i>Boolean</i>
<a href="#iprestriction" title="IpRestriction">IpRestriction</a>: <i>
      - <a href="siteconfig-iprestriction.md">IpRestriction</a></i>
<a href="#linuxfxversion" title="LinuxFxVersion">LinuxFxVersion</a>: <i>String</i>
<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
<a href="#use32bitworkerprocess" title="Use32BitWorkerProcess">Use32BitWorkerProcess</a>: <i>Boolean</i>
<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>: <i>Boolean</i>
<a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="siteconfig-cors.md">Cors</a></i>
</pre>

## Properties

#### AlwaysOn

Should the Function App be loaded at all times? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpsState

State of FTP / FTPS service for this function app. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`.

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

_Type_: List of <a href="siteconfig-iprestriction.md">IpRestriction</a>

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

_Type_: List of <a href="siteconfig-cors.md">Cors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

