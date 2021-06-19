# TF::Akamai::AppsecAdvancedSettingsPrefetch

CloudFormation equivalent of akamai_appsec_advanced_settings_prefetch

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecAdvancedSettingsPrefetch",
    "Properties" : {
        "<a href="#allextensions" title="AllExtensions">AllExtensions</a>" : <i>Boolean</i>,
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#enableapplayer" title="EnableAppLayer">EnableAppLayer</a>" : <i>Boolean</i>,
        "<a href="#enableratecontrols" title="EnableRateControls">EnableRateControls</a>" : <i>Boolean</i>,
        "<a href="#extensions" title="Extensions">Extensions</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecAdvancedSettingsPrefetch
Properties:
    <a href="#allextensions" title="AllExtensions">AllExtensions</a>: <i>Boolean</i>
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#enableapplayer" title="EnableAppLayer">EnableAppLayer</a>: <i>Boolean</i>
    <a href="#enableratecontrols" title="EnableRateControls">EnableRateControls</a>: <i>Boolean</i>
    <a href="#extensions" title="Extensions">Extensions</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### AllExtensions

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAppLayer

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRateControls

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extensions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

