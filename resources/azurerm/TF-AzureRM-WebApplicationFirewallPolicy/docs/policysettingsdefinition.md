# TF::AzureRM::WebApplicationFirewallPolicy PolicySettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#fileuploadlimitinmb" title="FileUploadLimitInMb">FileUploadLimitInMb</a>" : <i>Double</i>,
    "<a href="#maxrequestbodysizeinkb" title="MaxRequestBodySizeInKb">MaxRequestBodySizeInKb</a>" : <i>Double</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#requestbodycheck" title="RequestBodyCheck">RequestBodyCheck</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#fileuploadlimitinmb" title="FileUploadLimitInMb">FileUploadLimitInMb</a>: <i>Double</i>
<a href="#maxrequestbodysizeinkb" title="MaxRequestBodySizeInKb">MaxRequestBodySizeInKb</a>: <i>Double</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#requestbodycheck" title="RequestBodyCheck">RequestBodyCheck</a>: <i>Boolean</i>
</pre>

## Properties

#### Enabled

Describes if the policy is in enabled state or disabled state. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUploadLimitInMb

The File Upload Limit in MB. Accepted values are in the range `1` to `750`. Defaults to `100`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestBodySizeInKb

The Maximum Request Body Size in KB.  Accepted values are in the range `8` to `128`. Defaults to `128`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Describes if it is in detection mode or prevention mode at the policy level. Defaults to `Prevention`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBodyCheck

Is Request Body Inspection enabled? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

