# Terraform::Google::AccessContextManagerAccessLevel Conditions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipsubnetworks" title="IpSubnetworks">IpSubnetworks</a>" : <i>[ String, ... ]</i>,
    "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
    "<a href="#negate" title="Negate">Negate</a>" : <i>Boolean</i>,
    "<a href="#requiredaccesslevels" title="RequiredAccessLevels">RequiredAccessLevels</a>" : <i>[ String, ... ]</i>,
    "<a href="#devicepolicy" title="DevicePolicy">DevicePolicy</a>" : <i>[ &lt;a href=&#34;conditions-devicepolicy.md&#34;&gt;DevicePolicy&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipsubnetworks" title="IpSubnetworks">IpSubnetworks</a>: <i>
      - String</i>
<a href="#members" title="Members">Members</a>: <i>
      - String</i>
<a href="#negate" title="Negate">Negate</a>: <i>Boolean</i>
<a href="#requiredaccesslevels" title="RequiredAccessLevels">RequiredAccessLevels</a>: <i>
      - String</i>
<a href="#devicepolicy" title="DevicePolicy">DevicePolicy</a>: <i>
      - &lt;a href=&#34;conditions-devicepolicy.md&#34;&gt;DevicePolicy&lt;/a&gt;</i>
</pre>

## Properties

#### IpSubnetworks

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negate

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredAccessLevels

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevicePolicy

_Required_: No
_Type_: List of &lt;a href=&#34;conditions-devicepolicy.md&#34;&gt;DevicePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

