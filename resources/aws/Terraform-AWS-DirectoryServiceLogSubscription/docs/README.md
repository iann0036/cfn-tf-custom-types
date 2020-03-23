# Terraform::AWS::DirectoryServiceLogSubscription

Provides a Log subscription for AWS Directory Service that pushes logs to cloudwatch.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DirectoryServiceLogSubscription",
    "Properties" : {
        "<a href="#directoryid" title="DirectoryId">DirectoryId</a>" : <i>String</i>,
        "<a href="#loggroupname" title="LogGroupName">LogGroupName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DirectoryServiceLogSubscription
Properties:
    <a href="#directoryid" title="DirectoryId">DirectoryId</a>: <i>String</i>
    <a href="#loggroupname" title="LogGroupName">LogGroupName</a>: <i>String</i>
</pre>

## Properties

#### DirectoryId

The id of directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogGroupName

Name of the cloudwatch log group to which the logs should be published. The log group should be already created and the directory service principal should be provided with required permission to create stream and publish logs. Changing this value would delete the current subscription and create a new one. A directory can only have one log subscription at a time.

_Required_: Yes

_Type_: String

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

