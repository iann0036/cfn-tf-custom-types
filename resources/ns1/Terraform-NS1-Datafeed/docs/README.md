# Terraform::NS1::Datafeed

Provides a NS1 Data Feed resource. This can be used to create, modify, and delete data feeds.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NS1::Datafeed",
    "Properties" : {
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sourceid" title="SourceId">SourceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NS1::Datafeed
Properties:
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="config.md">Config</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sourceid" title="SourceId">SourceId</a>: <i>String</i>
</pre>

## Properties

#### Config

The feeds configuration matching the specification in
`feed_config` from /data/sourcetypes.

_Required_: No

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The free form name of the data feed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceId

The data source id that this feed is connected to.

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

