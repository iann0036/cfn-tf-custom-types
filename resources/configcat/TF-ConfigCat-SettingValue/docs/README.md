# TF::ConfigCat::SettingValue

CloudFormation equivalent of configcat_setting_value

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ConfigCat::SettingValue",
    "Properties" : {
        "<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>" : <i>String</i>,
        "<a href="#initonly" title="InitOnly">InitOnly</a>" : <i>Boolean</i>,
        "<a href="#mandatorynotes" title="MandatoryNotes">MandatoryNotes</a>" : <i>String</i>,
        "<a href="#settingid" title="SettingId">SettingId</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#percentageitems" title="PercentageItems">PercentageItems</a>" : <i>[ <a href="percentageitemsdefinition.md">PercentageItemsDefinition</a>, ... ]</i>,
        "<a href="#rolloutrules" title="RolloutRules">RolloutRules</a>" : <i>[ <a href="rolloutrulesdefinition.md">RolloutRulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ConfigCat::SettingValue
Properties:
    <a href="#environmentid" title="EnvironmentId">EnvironmentId</a>: <i>String</i>
    <a href="#initonly" title="InitOnly">InitOnly</a>: <i>Boolean</i>
    <a href="#mandatorynotes" title="MandatoryNotes">MandatoryNotes</a>: <i>String</i>
    <a href="#settingid" title="SettingId">SettingId</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#percentageitems" title="PercentageItems">PercentageItems</a>: <i>
      - <a href="percentageitemsdefinition.md">PercentageItemsDefinition</a></i>
    <a href="#rolloutrules" title="RolloutRules">RolloutRules</a>: <i>
      - <a href="rolloutrulesdefinition.md">RolloutRulesDefinition</a></i>
</pre>

## Properties

#### EnvironmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MandatoryNotes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SettingId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PercentageItems

_Required_: No

_Type_: List of <a href="percentageitemsdefinition.md">PercentageItemsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RolloutRules

_Required_: No

_Type_: List of <a href="rolloutrulesdefinition.md">RolloutRulesDefinition</a>

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

#### SettingType

Returns the <code>SettingType</code> value.

