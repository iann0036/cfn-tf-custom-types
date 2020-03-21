# Terraform::AzureRM::ApiManagement HostnameConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#management" title="Management">Management</a>" : <i>[ <a href="hostnameconfiguration-management.md">Management</a>, ... ]</i>,
    "<a href="#portal" title="Portal">Portal</a>" : <i>[ <a href="hostnameconfiguration-portal.md">Portal</a>, ... ]</i>,
    "<a href="#proxy" title="Proxy">Proxy</a>" : <i>[ <a href="hostnameconfiguration-proxy.md">Proxy</a>, ... ]</i>,
    "<a href="#scm" title="Scm">Scm</a>" : <i>[ <a href="hostnameconfiguration-scm.md">Scm</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#management" title="Management">Management</a>: <i>
      - <a href="hostnameconfiguration-management.md">Management</a></i>
<a href="#portal" title="Portal">Portal</a>: <i>
      - <a href="hostnameconfiguration-portal.md">Portal</a></i>
<a href="#proxy" title="Proxy">Proxy</a>: <i>
      - <a href="hostnameconfiguration-proxy.md">Proxy</a></i>
<a href="#scm" title="Scm">Scm</a>: <i>
      - <a href="hostnameconfiguration-scm.md">Scm</a></i>
</pre>

## Properties

#### Management

_Required_: No
_Type_: List of <a href="hostnameconfiguration-management.md">Management</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portal

_Required_: No
_Type_: List of <a href="hostnameconfiguration-portal.md">Portal</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No
_Type_: List of <a href="hostnameconfiguration-proxy.md">Proxy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scm

_Required_: No
_Type_: List of <a href="hostnameconfiguration-scm.md">Scm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

