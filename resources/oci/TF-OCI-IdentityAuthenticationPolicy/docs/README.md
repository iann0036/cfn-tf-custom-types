# TF::OCI::IdentityAuthenticationPolicy

This resource provides the Authentication Policy resource in Oracle Cloud Infrastructure Identity service.

Updates authentication policy for the specified tenancy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::IdentityAuthenticationPolicy",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>[ <a href="networkpolicydefinition.md">NetworkPolicyDefinition</a>, ... ]</i>,
        "<a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>" : <i>[ <a href="passwordpolicydefinition.md">PasswordPolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::IdentityAuthenticationPolicy
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>: <i>
      - <a href="networkpolicydefinition.md">NetworkPolicyDefinition</a></i>
    <a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>: <i>
      - <a href="passwordpolicydefinition.md">PasswordPolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

The OCID of the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicy

_Required_: No

_Type_: List of <a href="networkpolicydefinition.md">NetworkPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordPolicy

_Required_: No

_Type_: List of <a href="passwordpolicydefinition.md">PasswordPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

