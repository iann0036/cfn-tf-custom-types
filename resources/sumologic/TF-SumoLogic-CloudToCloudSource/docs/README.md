# TF::SumoLogic::CloudToCloudSource

Provides a [Sumologic Cloud-to-Cloud source][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::CloudToCloudSource",
    "Properties" : {
        "<a href="#collectorid" title="CollectorId">CollectorId</a>" : <i>Double</i>,
        "<a href="#config" title="Config">Config</a>" : <i>String</i>,
        "<a href="#schemaref" title="SchemaRef">SchemaRef</a>" : <i>[ <a href="schemarefdefinition.md">SchemaRefDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::CloudToCloudSource
Properties:
    <a href="#collectorid" title="CollectorId">CollectorId</a>: <i>Double</i>
    <a href="#config" title="Config">Config</a>: <i>String</i>
    <a href="#schemaref" title="SchemaRef">SchemaRef</a>: <i>
      - <a href="schemarefdefinition.md">SchemaRefDefinition</a></i>
</pre>

## Properties

#### CollectorId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaRef

_Required_: Yes

_Type_: List of <a href="schemarefdefinition.md">SchemaRefDefinition</a>

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

