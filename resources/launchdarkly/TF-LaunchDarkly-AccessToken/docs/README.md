# TF::LaunchDarkly::AccessToken

CloudFormation equivalent of launchdarkly_access_token

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::LaunchDarkly::AccessToken",
    "Properties" : {
        "<a href="#customroles" title="CustomRoles">CustomRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultapiversion" title="DefaultApiVersion">DefaultApiVersion</a>" : <i>Double</i>,
        "<a href="#expire" title="Expire">Expire</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#servicetoken" title="ServiceToken">ServiceToken</a>" : <i>Boolean</i>,
        "<a href="#policystatements" title="PolicyStatements">PolicyStatements</a>" : <i>[ <a href="policystatementsdefinition.md">PolicyStatementsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::LaunchDarkly::AccessToken
Properties:
    <a href="#customroles" title="CustomRoles">CustomRoles</a>: <i>
      - String</i>
    <a href="#defaultapiversion" title="DefaultApiVersion">DefaultApiVersion</a>: <i>Double</i>
    <a href="#expire" title="Expire">Expire</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#servicetoken" title="ServiceToken">ServiceToken</a>: <i>Boolean</i>
    <a href="#policystatements" title="PolicyStatements">PolicyStatements</a>: <i>
      - <a href="policystatementsdefinition.md">PolicyStatementsDefinition</a></i>
</pre>

## Properties

#### CustomRoles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultApiVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expire

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceToken

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyStatements

_Required_: No

_Type_: List of <a href="policystatementsdefinition.md">PolicyStatementsDefinition</a>

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

#### Token

Returns the <code>Token</code> value.

