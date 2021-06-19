# TF::Alicloud::CmsSiteMonitor

This resource provides a site monitor resource and it can be used to monitor public endpoints and websites.
Details at https://www.alibabacloud.com/help/doc-detail/67907.htm

Available in 1.72.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CmsSiteMonitor",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#alertids" title="AlertIds">AlertIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#optionsjson" title="OptionsJson">OptionsJson</a>" : <i>String</i>,
        "<a href="#taskname" title="TaskName">TaskName</a>" : <i>String</i>,
        "<a href="#tasktype" title="TaskType">TaskType</a>" : <i>String</i>,
        "<a href="#ispcities" title="IspCities">IspCities</a>" : <i>[ <a href="ispcitiesdefinition.md">IspCitiesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CmsSiteMonitor
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#alertids" title="AlertIds">AlertIds</a>: <i>
      - String</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#optionsjson" title="OptionsJson">OptionsJson</a>: <i>String</i>
    <a href="#taskname" title="TaskName">TaskName</a>: <i>String</i>
    <a href="#tasktype" title="TaskType">TaskType</a>: <i>String</i>
    <a href="#ispcities" title="IspCities">IspCities</a>: <i>
      - <a href="ispcitiesdefinition.md">IspCitiesDefinition</a></i>
</pre>

## Properties

#### Address

The URL or IP address monitored by the site monitoring task.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertIds

The IDs of existing alert rules to be associated with the site monitoring task.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The monitoring interval of the site monitoring task. Unit: minutes. Valid values: 1, 5, and 15. Default value: 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionsJson

The extended options of the protocol of the site monitoring task. The options vary according to the protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskName

The name of the site monitoring task. The name must be 4 to 100 characters in length. The name can contain the following types of characters: letters, digits, and underscores.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskType

The protocol of the site monitoring task. Currently, site monitoring supports the following protocols: HTTP, Ping, TCP, UDP, DNS, SMTP, POP3, and FTP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IspCities

_Required_: No

_Type_: List of <a href="ispcitiesdefinition.md">IspCitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### TaskState

Returns the <code>TaskState</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

