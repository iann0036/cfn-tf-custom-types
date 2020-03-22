# Terraform::AzureRM::ApiManagementApi

Manages an API within an API Management Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApiManagementApi",
    "Properties" : {
        "<a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ String, ... ]</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#revision" title="Revision">Revision</a>" : <i>String</i>,
        "<a href="#serviceurl" title="ServiceUrl">ServiceUrl</a>" : <i>String</i>,
        "<a href="#soappassthrough" title="SoapPassThrough">SoapPassThrough</a>" : <i>Boolean</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#versionsetid" title="VersionSetId">VersionSetId</a>" : <i>String</i>,
        "<a href="#import" title="Import">Import</a>" : <i>[ <a href="import.md">Import</a>, ... ]</i>,
        "<a href="#subscriptionkeyparameternames" title="SubscriptionKeyParameterNames">SubscriptionKeyParameterNames</a>" : <i>[ <a href="subscriptionkeyparameternames.md">SubscriptionKeyParameterNames</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#wsdlselector" title="WsdlSelector">WsdlSelector</a>" : <i>[ <a href="wsdlselector.md">WsdlSelector</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApiManagementApi
Properties:
    <a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#protocols" title="Protocols">Protocols</a>: <i>
      - String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#revision" title="Revision">Revision</a>: <i>String</i>
    <a href="#serviceurl" title="ServiceUrl">ServiceUrl</a>: <i>String</i>
    <a href="#soappassthrough" title="SoapPassThrough">SoapPassThrough</a>: <i>Boolean</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#versionsetid" title="VersionSetId">VersionSetId</a>: <i>String</i>
    <a href="#import" title="Import">Import</a>: <i>
      - <a href="import.md">Import</a></i>
    <a href="#subscriptionkeyparameternames" title="SubscriptionKeyParameterNames">SubscriptionKeyParameterNames</a>: <i>
      - <a href="subscriptionkeyparameternames.md">SubscriptionKeyParameterNames</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#wsdlselector" title="WsdlSelector">WsdlSelector</a>: <i>
      - <a href="wsdlselector.md">WsdlSelector</a></i>
</pre>

## Properties

#### ApiManagementName

The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the API Management API, which may include HTML formatting tags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of the API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the API Management API. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of it's resource paths within the API Management Service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

A list of protocols the operations in this API can be invoked. Possible values are `http` and `https`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

The Revision which used for this API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceUrl

Absolute URL of the backend service implementing this API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoapPassThrough

Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The Version number of this API, if this API is versioned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionSetId

The ID of the Version Set which this API is associated with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Import

_Required_: No

_Type_: List of <a href="import.md">Import</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionKeyParameterNames

_Required_: No

_Type_: List of <a href="subscriptionkeyparameternames.md">SubscriptionKeyParameterNames</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WsdlSelector

_Required_: No

_Type_: List of <a href="wsdlselector.md">WsdlSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### IsCurrent

Returns the <code>IsCurrent</code> value.

#### IsOnline

Returns the <code>IsOnline</code> value.

