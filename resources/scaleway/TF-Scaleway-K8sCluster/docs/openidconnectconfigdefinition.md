# TF::Scaleway::K8sCluster OpenIdConnectConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#groupsclaim" title="GroupsClaim">GroupsClaim</a>" : <i>[ String, ... ]</i>,
    "<a href="#groupsprefix" title="GroupsPrefix">GroupsPrefix</a>" : <i>String</i>,
    "<a href="#issuerurl" title="IssuerUrl">IssuerUrl</a>" : <i>String</i>,
    "<a href="#requiredclaim" title="RequiredClaim">RequiredClaim</a>" : <i>[ String, ... ]</i>,
    "<a href="#usernameclaim" title="UsernameClaim">UsernameClaim</a>" : <i>String</i>,
    "<a href="#usernameprefix" title="UsernamePrefix">UsernamePrefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#groupsclaim" title="GroupsClaim">GroupsClaim</a>: <i>
      - String</i>
<a href="#groupsprefix" title="GroupsPrefix">GroupsPrefix</a>: <i>String</i>
<a href="#issuerurl" title="IssuerUrl">IssuerUrl</a>: <i>String</i>
<a href="#requiredclaim" title="RequiredClaim">RequiredClaim</a>: <i>
      - String</i>
<a href="#usernameclaim" title="UsernameClaim">UsernameClaim</a>: <i>String</i>
<a href="#usernameprefix" title="UsernamePrefix">UsernamePrefix</a>: <i>String</i>
</pre>

## Properties

#### ClientId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsClaim

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredClaim

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameClaim

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

