# TF::AzureCAF::Name

The resource azurecaf_name implements a set of methodologies to apply consistent resource naming using the default Microsoft Cloud Adoption Framework for Azure recommendations as per [naming-and-tagging](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/naming-and-tagging).

the azurecaf_name supersedes the previous azurecaf_naming_convention. This new resource provides more flexibility and will be updated on a regular basis as new Azure services are released.

The azurecaf_name resource allows you to:

* Clean inputs to make sure they remain compliant with the allowed patterns for each Azure resource
* Generate random characters to append at the end of the resource name
* Handle prefix, suffixes (either manual or as per the Azure cloud adoption framework resource conventions)
* Allow passthrough mode (simply validate the output)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureCAF::Name",
    "Properties" : {
        "<a href="#cleaninput" title="CleanInput">CleanInput</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#passthrough" title="Passthrough">Passthrough</a>" : <i>Boolean</i>,
        "<a href="#prefixes" title="Prefixes">Prefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#randomlength" title="RandomLength">RandomLength</a>" : <i>Double</i>,
        "<a href="#randomseed" title="RandomSeed">RandomSeed</a>" : <i>Double</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#separator" title="Separator">Separator</a>" : <i>String</i>,
        "<a href="#suffixes" title="Suffixes">Suffixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#useslug" title="UseSlug">UseSlug</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureCAF::Name
Properties:
    <a href="#cleaninput" title="CleanInput">CleanInput</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#passthrough" title="Passthrough">Passthrough</a>: <i>Boolean</i>
    <a href="#prefixes" title="Prefixes">Prefixes</a>: <i>
      - String</i>
    <a href="#randomlength" title="RandomLength">RandomLength</a>: <i>Double</i>
    <a href="#randomseed" title="RandomSeed">RandomSeed</a>: <i>Double</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>: <i>
      - String</i>
    <a href="#separator" title="Separator">Separator</a>: <i>String</i>
    <a href="#suffixes" title="Suffixes">Suffixes</a>: <i>
      - String</i>
    <a href="#useslug" title="UseSlug">UseSlug</a>: <i>Boolean</i>
</pre>

## Properties

#### CleanInput

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passthrough

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RandomLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RandomSeed

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Separator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suffixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSlug

_Required_: No

_Type_: Boolean

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

#### Result

Returns the <code>Result</code> value.

#### Results

Returns the <code>Results</code> value.

