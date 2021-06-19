# TF::AWS::Kinesisanalyticsv2Application RecordColumnDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mapping" title="Mapping">Mapping</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sqltype" title="SqlType">SqlType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#mapping" title="Mapping">Mapping</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sqltype" title="SqlType">SqlType</a>: <i>String</i>
</pre>

## Properties

#### Mapping

A reference to the data element in the streaming input or the reference data source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the column that is created in the in-application input stream or reference table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlType

The type of column created in the in-application input stream or reference table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

