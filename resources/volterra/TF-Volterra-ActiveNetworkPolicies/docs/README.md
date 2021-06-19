# TF::Volterra::ActiveNetworkPolicies

CloudFormation equivalent of volterra_active_network_policies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::ActiveNetworkPolicies",
    "Properties" : {
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ <a href="policiesdefinition.md">PoliciesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::ActiveNetworkPolicies
Properties:
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - <a href="policiesdefinition.md">PoliciesDefinition</a></i>
</pre>

## Properties

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of <a href="policiesdefinition.md">PoliciesDefinition</a>

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

