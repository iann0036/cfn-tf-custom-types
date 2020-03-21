# Terraform::AWS::DbOptionGroup Option

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dbsecuritygroupmemberships" title="DbSecurityGroupMemberships">DbSecurityGroupMemberships</a>" : <i>[ String, ... ]</i>,
    "<a href="#optionname" title="OptionName">OptionName</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#vpcsecuritygroupmemberships" title="VpcSecurityGroupMemberships">VpcSecurityGroupMemberships</a>" : <i>[ String, ... ]</i>,
    "<a href="#optionsettings" title="OptionSettings">OptionSettings</a>" : <i>[ <a href="option-optionsettings.md">OptionSettings</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dbsecuritygroupmemberships" title="DbSecurityGroupMemberships">DbSecurityGroupMemberships</a>: <i>
      - String</i>
<a href="#optionname" title="OptionName">OptionName</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#vpcsecuritygroupmemberships" title="VpcSecurityGroupMemberships">VpcSecurityGroupMemberships</a>: <i>
      - String</i>
<a href="#optionsettings" title="OptionSettings">OptionSettings</a>: <i>
      - <a href="option-optionsettings.md">OptionSettings</a></i>
</pre>

## Properties

#### DbSecurityGroupMemberships

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSecurityGroupMemberships

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionSettings

_Required_: No
_Type_: List of <a href="option-optionsettings.md">OptionSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

