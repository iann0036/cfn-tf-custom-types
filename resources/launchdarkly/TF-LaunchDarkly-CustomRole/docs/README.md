# TF::LaunchDarkly::CustomRole

Provides a LaunchDarkly custom role resource.

This resource allows you to create and manage custom roles within your LaunchDarkly organization.

-> **Note:** Custom roles are only available to customers on enterprise plans. To learn more about enterprise plans, contact sales@launchdarkly.com.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::LaunchDarkly::CustomRole",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policydefinition.md">PolicyDefinition</a>, ... ]</i>,
        "<a href="#policystatements" title="PolicyStatements">PolicyStatements</a>" : <i>[ <a href="policystatementsdefinition.md">PolicyStatementsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::LaunchDarkly::CustomRole
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policydefinition.md">PolicyDefinition</a></i>
    <a href="#policystatements" title="PolicyStatements">PolicyStatements</a>: <i>
      - <a href="policystatementsdefinition.md">PolicyStatementsDefinition</a></i>
</pre>

## Properties

#### Description

The description of the custom role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The unique key that references the custom role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name for the custom role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: List of <a href="policydefinition.md">PolicyDefinition</a>

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

