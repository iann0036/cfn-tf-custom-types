# TF::MSO::SchemaTemplateContractServiceGraph

CloudFormation equivalent of mso_schema_template_contract_service_graph

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaTemplateContractServiceGraph",
    "Properties" : {
        "<a href="#contractname" title="ContractName">ContractName</a>" : <i>String</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#servicegraphname" title="ServiceGraphName">ServiceGraphName</a>" : <i>String</i>,
        "<a href="#servicegraphschemaid" title="ServiceGraphSchemaId">ServiceGraphSchemaId</a>" : <i>String</i>,
        "<a href="#servicegraphsiteid" title="ServiceGraphSiteId">ServiceGraphSiteId</a>" : <i>String</i>,
        "<a href="#servicegraphtemplatename" title="ServiceGraphTemplateName">ServiceGraphTemplateName</a>" : <i>String</i>,
        "<a href="#siteid" title="SiteId">SiteId</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#noderelationship" title="NodeRelationship">NodeRelationship</a>" : <i>[ <a href="noderelationshipdefinition.md">NodeRelationshipDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaTemplateContractServiceGraph
Properties:
    <a href="#contractname" title="ContractName">ContractName</a>: <i>String</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#servicegraphname" title="ServiceGraphName">ServiceGraphName</a>: <i>String</i>
    <a href="#servicegraphschemaid" title="ServiceGraphSchemaId">ServiceGraphSchemaId</a>: <i>String</i>
    <a href="#servicegraphsiteid" title="ServiceGraphSiteId">ServiceGraphSiteId</a>: <i>String</i>
    <a href="#servicegraphtemplatename" title="ServiceGraphTemplateName">ServiceGraphTemplateName</a>: <i>String</i>
    <a href="#siteid" title="SiteId">SiteId</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#noderelationship" title="NodeRelationship">NodeRelationship</a>: <i>
      - <a href="noderelationshipdefinition.md">NodeRelationshipDefinition</a></i>
</pre>

## Properties

#### ContractName

_Required_: Yes

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

#### ServiceGraphSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGraphSiteId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGraphTemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeRelationship

_Required_: No

_Type_: List of <a href="noderelationshipdefinition.md">NodeRelationshipDefinition</a>

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

