# TF::AzureRM::DataFactoryLinkedServiceAzureSearch

Manages a Linked Service (connection) between Azure Search Service and Azure Data Factory.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::DataFactoryLinkedServiceAzureSearch",
    "Properties" : {
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>[ <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a>, ... ]</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ String, ... ]</i>,
        "<a href="#datafactoryid" title="DataFactoryId">DataFactoryId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#integrationruntimename" title="IntegrationRuntimeName">IntegrationRuntimeName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#searchservicekey" title="SearchServiceKey">SearchServiceKey</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::DataFactoryLinkedServiceAzureSearch
Properties:
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>
      - <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a></i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - String</i>
    <a href="#datafactoryid" title="DataFactoryId">DataFactoryId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#integrationruntimename" title="IntegrationRuntimeName">IntegrationRuntimeName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#searchservicekey" title="SearchServiceKey">SearchServiceKey</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdditionalProperties

A map of additional properties to associate with the Data Factory Linked Service.

_Required_: No

_Type_: List of <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

List of tags that can be used for describing the Data Factory Linked Service.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFactoryId

The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the Data Factory Linked Service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRuntimeName

The integration runtime reference to associate with the Data Factory Linked Service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Data Factory Linked Service. Changing this forces a new resource to be created. Must be unique within a data
factory. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

A map of parameters to associate with the Data Factory Linked Service.

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchServiceKey

The key of the Azure Search Service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The URL of the Search Service endpoint (e.g. https://{searchServiceName}.search.windows.net).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EncryptedCredential

Returns the <code>EncryptedCredential</code> value.

#### Id

Returns the <code>Id</code> value.

