# TF::GoogleBeta::GoogleProjectOrganizationPolicy

CloudFormation equivalent of google_project_organization_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleProjectOrganizationPolicy",
    "Properties" : {
        "<a href="#constraint" title="Constraint">Constraint</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#booleanpolicy" title="BooleanPolicy">BooleanPolicy</a>" : <i>[ <a href="booleanpolicydefinition.md">BooleanPolicyDefinition</a>, ... ]</i>,
        "<a href="#listpolicy" title="ListPolicy">ListPolicy</a>" : <i>[ <a href="listpolicydefinition.md">ListPolicyDefinition</a>, ... ]</i>,
        "<a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>" : <i>[ <a href="restorepolicydefinition.md">RestorePolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleProjectOrganizationPolicy
Properties:
    <a href="#constraint" title="Constraint">Constraint</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#booleanpolicy" title="BooleanPolicy">BooleanPolicy</a>: <i>
      - <a href="booleanpolicydefinition.md">BooleanPolicyDefinition</a></i>
    <a href="#listpolicy" title="ListPolicy">ListPolicy</a>: <i>
      - <a href="listpolicydefinition.md">ListPolicyDefinition</a></i>
    <a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>: <i>
      - <a href="restorepolicydefinition.md">RestorePolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Constraint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BooleanPolicy

_Required_: No

_Type_: List of <a href="booleanpolicydefinition.md">BooleanPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListPolicy

_Required_: No

_Type_: List of <a href="listpolicydefinition.md">ListPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestorePolicy

_Required_: No

_Type_: List of <a href="restorepolicydefinition.md">RestorePolicyDefinition</a>

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

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.
