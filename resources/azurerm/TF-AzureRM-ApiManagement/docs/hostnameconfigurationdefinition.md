# TF::AzureRM::ApiManagement HostnameConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#developerportal" title="DeveloperPortal">DeveloperPortal</a>" : <i>[ <a href="developerportaldefinition.md">DeveloperPortalDefinition</a>, ... ]</i>,
    "<a href="#management" title="Management">Management</a>" : <i>[ <a href="managementdefinition.md">ManagementDefinition</a>, ... ]</i>,
    "<a href="#portal" title="Portal">Portal</a>" : <i>[ <a href="portaldefinition.md">PortalDefinition</a>, ... ]</i>,
    "<a href="#proxy" title="Proxy">Proxy</a>" : <i>[ <a href="proxydefinition.md">ProxyDefinition</a>, ... ]</i>,
    "<a href="#scm" title="Scm">Scm</a>" : <i>[ <a href="scmdefinition.md">ScmDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
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
</pre>

## Properties

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

