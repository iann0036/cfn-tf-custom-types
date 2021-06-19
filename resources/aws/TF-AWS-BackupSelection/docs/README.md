# TF::AWS::BackupSelection

Manages selection conditions for AWS Backup plan resources.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::BackupSelection",
    "Properties" : {
        "<a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#planid" title="PlanId">PlanId</a>" : <i>String</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
        "<a href="#selectiontag" title="SelectionTag">SelectionTag</a>" : <i>[ <a href="selectiontagdefinition.md">SelectionTagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::BackupSelection
Properties:
    <a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#planid" title="PlanId">PlanId</a>: <i>String</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
    <a href="#selectiontag" title="SelectionTag">SelectionTag</a>: <i>
      - <a href="selectiontagdefinition.md">SelectionTagDefinition</a></i>
</pre>

## Properties

#### IamRoleArn

The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The display name of a resource selection document.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlanId

The backup plan ID to be associated with the selection of resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectionTag

_Required_: No

_Type_: List of <a href="selectiontagdefinition.md">SelectionTagDefinition</a>

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

