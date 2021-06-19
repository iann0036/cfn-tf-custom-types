# TF::MSO::SchemaTemplateServiceGraph

CloudFormation equivalent of mso_schema_template_service_graph

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaTemplateServiceGraph",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#servicegraphname" title="ServiceGraphName">ServiceGraphName</a>" : <i>String</i>,
        "<a href="#servicenodetype" title="ServiceNodeType">ServiceNodeType</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#sitenodes" title="SiteNodes">SiteNodes</a>" : <i>[ <a href="sitenodesdefinition.md">SiteNodesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaTemplateServiceGraph
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#servicegraphname" title="ServiceGraphName">ServiceGraphName</a>: <i>String</i>
    <a href="#servicenodetype" title="ServiceNodeType">ServiceNodeType</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#sitenodes" title="SiteNodes">SiteNodes</a>: <i>
      - <a href="sitenodesdefinition.md">SiteNodesDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGraphName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNodeType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteNodes

_Required_: No

_Type_: List of <a href="sitenodesdefinition.md">SiteNodesDefinition</a>

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

