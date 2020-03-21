# Terraform::Google::AppEngineStandardAppVersion

CloudFormation equivalent of google_app_engine_standard_app_version

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::AppEngineStandardAppVersion",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#envvariables" title="EnvVariables">EnvVariables</a>" : <i>[ &lt;a href=&#34;envvariables.md&#34;&gt;EnvVariables&lt;/a&gt;, ... ]</i>,
        "<a href="#instanceclass" title="InstanceClass">InstanceClass</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#threadsafe" title="Threadsafe">Threadsafe</a>" : <i>Boolean</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#deployment" title="Deployment">Deployment</a>" : <i>[ &lt;a href=&#34;deployment.md&#34;&gt;Deployment&lt;/a&gt;, ... ]</i>,
        "<a href="#entrypoint" title="Entrypoint">Entrypoint</a>" : <i>[ &lt;a href=&#34;entrypoint.md&#34;&gt;Entrypoint&lt;/a&gt;, ... ]</i>,
        "<a href="#handlers" title="Handlers">Handlers</a>" : <i>[ &lt;a href=&#34;handlers.md&#34;&gt;Handlers&lt;/a&gt;, ... ]</i>,
        "<a href="#libraries" title="Libraries">Libraries</a>" : <i>[ &lt;a href=&#34;libraries.md&#34;&gt;Libraries&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#files" title="Files">Files</a>" : <i>[ &lt;a href=&#34;files.md&#34;&gt;Files&lt;/a&gt;, ... ]</i>,
        "<a href="#zip" title="Zip">Zip</a>" : <i>[ &lt;a href=&#34;zip.md&#34;&gt;Zip&lt;/a&gt;, ... ]</i>,
        "<a href="#script" title="Script">Script</a>" : <i>[ &lt;a href=&#34;script.md&#34;&gt;Script&lt;/a&gt;, ... ]</i>,
        "<a href="#staticfiles" title="StaticFiles">StaticFiles</a>" : <i>[ &lt;a href=&#34;staticfiles.md&#34;&gt;StaticFiles&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::AppEngineStandardAppVersion
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>: <i>Boolean</i>
    <a href="#envvariables" title="EnvVariables">EnvVariables</a>: <i>
      - &lt;a href=&#34;envvariables.md&#34;&gt;EnvVariables&lt;/a&gt;</i>
    <a href="#instanceclass" title="InstanceClass">InstanceClass</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#threadsafe" title="Threadsafe">Threadsafe</a>: <i>Boolean</i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#deployment" title="Deployment">Deployment</a>: <i>
      - &lt;a href=&#34;deployment.md&#34;&gt;Deployment&lt;/a&gt;</i>
    <a href="#entrypoint" title="Entrypoint">Entrypoint</a>: <i>
      - &lt;a href=&#34;entrypoint.md&#34;&gt;Entrypoint&lt;/a&gt;</i>
    <a href="#handlers" title="Handlers">Handlers</a>: <i>
      - &lt;a href=&#34;handlers.md&#34;&gt;Handlers&lt;/a&gt;</i>
    <a href="#libraries" title="Libraries">Libraries</a>: <i>
      - &lt;a href=&#34;libraries.md&#34;&gt;Libraries&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#files" title="Files">Files</a>: <i>
      - &lt;a href=&#34;files.md&#34;&gt;Files&lt;/a&gt;</i>
    <a href="#zip" title="Zip">Zip</a>: <i>
      - &lt;a href=&#34;zip.md&#34;&gt;Zip&lt;/a&gt;</i>
    <a href="#script" title="Script">Script</a>: <i>
      - &lt;a href=&#34;script.md&#34;&gt;Script&lt;/a&gt;</i>
    <a href="#staticfiles" title="StaticFiles">StaticFiles</a>: <i>
      - &lt;a href=&#34;staticfiles.md&#34;&gt;StaticFiles&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteServiceOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvVariables

_Required_: No

_Type_: List of &lt;a href=&#34;envvariables.md&#34;&gt;EnvVariables&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoopOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threadsafe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deployment

_Required_: No

_Type_: List of &lt;a href=&#34;deployment.md&#34;&gt;Deployment&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entrypoint

_Required_: No

_Type_: List of &lt;a href=&#34;entrypoint.md&#34;&gt;Entrypoint&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handlers

_Required_: No

_Type_: List of &lt;a href=&#34;handlers.md&#34;&gt;Handlers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Libraries

_Required_: No

_Type_: List of &lt;a href=&#34;libraries.md&#34;&gt;Libraries&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Files

_Required_: No

_Type_: List of &lt;a href=&#34;files.md&#34;&gt;Files&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zip

_Required_: No

_Type_: List of &lt;a href=&#34;zip.md&#34;&gt;Zip&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: No

_Type_: List of &lt;a href=&#34;script.md&#34;&gt;Script&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticFiles

_Required_: No

_Type_: List of &lt;a href=&#34;staticfiles.md&#34;&gt;StaticFiles&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Name

Returns the &lt;code&gt;Name&lt;/code&gt; value.

