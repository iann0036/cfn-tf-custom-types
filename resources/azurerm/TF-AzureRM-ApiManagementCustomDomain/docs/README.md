# TF::AzureRM::ApiManagementCustomDomain

Manages a API Management Custom Domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::ApiManagementCustomDomain",
    "Properties" : {
        "<a href="#apimanagementid" title="ApiManagementId">ApiManagementId</a>" : <i>String</i>,
        "<a href="#developerportal" title="DeveloperPortal">DeveloperPortal</a>" : <i>[ <a href="developerportaldefinition.md">DeveloperPortalDefinition</a>, ... ]</i>,
        "<a href="#management" title="Management">Management</a>" : <i>[ <a href="managementdefinition.md">ManagementDefinition</a>, ... ]</i>,
        "<a href="#portal" title="Portal">Portal</a>" : <i>[ <a href="portaldefinition.md">PortalDefinition</a>, ... ]</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>[ <a href="proxydefinition.md">ProxyDefinition</a>, ... ]</i>,
        "<a href="#scm" title="Scm">Scm</a>" : <i>[ <a href="scmdefinition.md">ScmDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::ApiManagementCustomDomain
Properties:
    <a href="#apimanagementid" title="ApiManagementId">ApiManagementId</a>: <i>String</i>
    <a href="#developerportal" title="DeveloperPortal">DeveloperPortal</a>: <i>
      - <a href="developerportaldefinition.md">DeveloperPortalDefinition</a></i>
    <a href="#management" title="Management">Management</a>: <i>
      - <a href="managementdefinition.md">ManagementDefinition</a></i>
    <a href="#portal" title="Portal">Portal</a>: <i>
      - <a href="portaldefinition.md">PortalDefinition</a></i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>
      - <a href="proxydefinition.md">ProxyDefinition</a></i>
    <a href="#scm" title="Scm">Scm</a>: <i>
      - <a href="scmdefinition.md">ScmDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ApiManagementId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeveloperPortal

_Required_: No

_Type_: List of <a href="developerportaldefinition.md">DeveloperPortalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of <a href="managementdefinition.md">ManagementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portal

_Required_: No

_Type_: List of <a href="portaldefinition.md">PortalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: List of <a href="proxydefinition.md">ProxyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scm

_Required_: No

_Type_: List of <a href="scmdefinition.md">ScmDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

