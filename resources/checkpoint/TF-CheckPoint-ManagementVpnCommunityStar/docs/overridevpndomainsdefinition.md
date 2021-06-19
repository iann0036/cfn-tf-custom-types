# TF::CheckPoint::ManagementVpnCommunityStar OverrideVpnDomainsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#vpndomain" title="VpnDomain">VpnDomain</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#vpndomain" title="VpnDomain">VpnDomain</a>: <i>String</i>
</pre>

## Properties

#### Gateway

Participant gateway in override VPN domain identified by the name or UID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnDomain

VPN domain network identified by the name or UID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

