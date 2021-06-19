# TF::AWS::CodebuildWebhook

Manages a CodeBuild webhook, which is an endpoint accepted by the CodeBuild service to trigger builds from source code repositories. Depending on the source type of the CodeBuild project, the CodeBuild service may also automatically create and delete the actual repository webhook as well.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CodebuildWebhook",
    "Properties" : {
        "<a href="#branchfilter" title="BranchFilter">BranchFilter</a>" : <i>String</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#filtergroup" title="FilterGroup">FilterGroup</a>" : <i>[ <a href="filtergroupdefinition.md">FilterGroupDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CodebuildWebhook
Properties:
    <a href="#branchfilter" title="BranchFilter">BranchFilter</a>: <i>String</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#filtergroup" title="FilterGroup">FilterGroup</a>: <i>
      - <a href="filtergroupdefinition.md">FilterGroupDefinition</a></i>
</pre>

## Properties

#### BranchFilter

A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use `filter_group` over `branch_filter`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

The name of the build project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterGroup

_Required_: No

_Type_: List of <a href="filtergroupdefinition.md">FilterGroupDefinition</a>

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

#### PayloadUrl

Returns the <code>PayloadUrl</code> value.

#### Secret

Returns the <code>Secret</code> value.

#### Url

Returns the <code>Url</code> value.

