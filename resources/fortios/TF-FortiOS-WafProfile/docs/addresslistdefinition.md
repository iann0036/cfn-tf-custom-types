# TF::FortiOS::WafProfile AddressListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blockedlog" title="BlockedLog">BlockedLog</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#blockedaddress" title="BlockedAddress">BlockedAddress</a>" : <i>[ <a href="blockedaddressdefinition.md">BlockedAddressDefinition</a>, ... ]</i>,
    "<a href="#trustedaddress" title="TrustedAddress">TrustedAddress</a>" : <i>[ <a href="trustedaddressdefinition.md">TrustedAddressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#blockedlog" title="BlockedLog">BlockedLog</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#blockedaddress" title="BlockedAddress">BlockedAddress</a>: <i>
      - <a href="blockedaddressdefinition.md">BlockedAddressDefinition</a></i>
<a href="#trustedaddress" title="TrustedAddress">TrustedAddress</a>: <i>
      - <a href="trustedaddressdefinition.md">TrustedAddressDefinition</a></i>
</pre>

## Properties

#### BlockedLog

Enable/disable logging on blocked addresses. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Severity. Valid values: `high`, `medium`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Status. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockedAddress

_Required_: No

_Type_: List of <a href="blockedaddressdefinition.md">BlockedAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedAddress

_Required_: No

_Type_: List of <a href="trustedaddressdefinition.md">TrustedAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

