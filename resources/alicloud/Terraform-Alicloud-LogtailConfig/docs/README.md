# Terraform::Alicloud::LogtailConfig

The Logtail access service is a log collection agent provided by Log Service. 
You can use Logtail to collect logs from servers such as Alibaba Cloud Elastic
Compute Service (ECS) instances in real time in the Log Service console. [Refer to details](https://www.alibabacloud.com/help/doc-detail/29058.htm
)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::LogtailConfig",
    "Properties" : {
        "<a href="#inputdetail" title="InputDetail">InputDetail</a>" : <i>String</i>,
        "<a href="#inputtype" title="InputType">InputType</a>" : <i>String</i>,
        "<a href="#logsample" title="LogSample">LogSample</a>" : <i>String</i>,
        "<a href="#logstore" title="Logstore">Logstore</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outputtype" title="OutputType">OutputType</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::LogtailConfig
Properties:
    <a href="#inputdetail" title="InputDetail">InputDetail</a>: <i>String</i>
    <a href="#inputtype" title="InputType">InputType</a>: <i>String</i>
    <a href="#logsample" title="LogSample">LogSample</a>: <i>String</i>
    <a href="#logstore" title="Logstore">Logstore</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outputtype" title="OutputType">OutputType</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### InputDetail

The logtail configure the required JSON files. ([Refer to details](https://www.alibabacloud.com/help/doc-detail/29058.htm)).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputType

The input type. Currently only two types of files and plugin are supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSample

（Optional）The log sample of the Logtail configuration. The log size cannot exceed 1,000 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logstore

The log store name to the query index belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Logtail configuration name, which is unique in the same project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputType

The output type. Currently, only LogService is supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project name to the log store belongs.

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

