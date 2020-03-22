# Terraform::AWS::BackupSelection

CloudFormation equivalent of aws_backup_selection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::BackupSelection",
    "Properties" : {
        "<a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#planid" title="PlanId">PlanId</a>" : <i>String</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
        "<a href="#selectiontag" title="SelectionTag">SelectionTag</a>" : <i>[ <a href="selectiontag.md">SelectionTag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::BackupSelection
Properties:
    <a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#planid" title="PlanId">PlanId</a>: <i>String</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
    <a href="#selectiontag" title="SelectionTag">SelectionTag</a>: <i>
      - <a href="selectiontag.md">SelectionTag</a></i>
</pre>

## Properties

#### IamRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlanId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectionTag

_Required_: No

_Type_: List of <a href="selectiontag.md">SelectionTag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

