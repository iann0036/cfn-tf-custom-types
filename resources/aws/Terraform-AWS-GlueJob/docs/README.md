# Terraform::AWS::GlueJob

CloudFormation equivalent of aws_glue_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlueJob",
    "Properties" : {
        "<a href="#allocatedcapacity" title="AllocatedCapacity">AllocatedCapacity</a>" : <i>Double</i>,
        "<a href="#connections" title="Connections">Connections</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultarguments" title="DefaultArguments">DefaultArguments</a>" : <i>[ <a href="defaultarguments.md">DefaultArguments</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#glueversion" title="GlueVersion">GlueVersion</a>" : <i>String</i>,
        "<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>" : <i>Double</i>,
        "<a href="#maxretries" title="MaxRetries">MaxRetries</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numberofworkers" title="NumberOfWorkers">NumberOfWorkers</a>" : <i>Double</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#workertype" title="WorkerType">WorkerType</a>" : <i>String</i>,
        "<a href="#command" title="Command">Command</a>" : <i>[ <a href="command.md">Command</a>, ... ]</i>,
        "<a href="#executionproperty" title="ExecutionProperty">ExecutionProperty</a>" : <i>[ <a href="executionproperty.md">ExecutionProperty</a>, ... ]</i>,
        "<a href="#notificationproperty" title="NotificationProperty">NotificationProperty</a>" : <i>[ <a href="notificationproperty.md">NotificationProperty</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlueJob
Properties:
    <a href="#allocatedcapacity" title="AllocatedCapacity">AllocatedCapacity</a>: <i>Double</i>
    <a href="#connections" title="Connections">Connections</a>: <i>
      - String</i>
    <a href="#defaultarguments" title="DefaultArguments">DefaultArguments</a>: <i>
      - <a href="defaultarguments.md">DefaultArguments</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#glueversion" title="GlueVersion">GlueVersion</a>: <i>String</i>
    <a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>: <i>Double</i>
    <a href="#maxretries" title="MaxRetries">MaxRetries</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numberofworkers" title="NumberOfWorkers">NumberOfWorkers</a>: <i>Double</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#workertype" title="WorkerType">WorkerType</a>: <i>String</i>
    <a href="#command" title="Command">Command</a>: <i>
      - <a href="command.md">Command</a></i>
    <a href="#executionproperty" title="ExecutionProperty">ExecutionProperty</a>: <i>
      - <a href="executionproperty.md">ExecutionProperty</a></i>
    <a href="#notificationproperty" title="NotificationProperty">NotificationProperty</a>: <i>
      - <a href="notificationproperty.md">NotificationProperty</a></i>
</pre>

## Properties

#### AllocatedCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Connections

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultArguments

_Required_: No

_Type_: List of <a href="defaultarguments.md">DefaultArguments</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlueVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfWorkers

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No

_Type_: List of <a href="command.md">Command</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionProperty

_Required_: No

_Type_: List of <a href="executionproperty.md">ExecutionProperty</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationProperty

_Required_: No

_Type_: List of <a href="notificationproperty.md">NotificationProperty</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

