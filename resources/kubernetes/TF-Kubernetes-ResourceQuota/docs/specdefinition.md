# TF::Kubernetes::ResourceQuota SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hard" title="Hard">Hard</a>" : <i>[ <a href="harddefinition.md">HardDefinition</a>, ... ]</i>,
    "<a href="#scopes" title="Scopes">Scopes</a>" : <i>[ String, ... ]</i>,
    "<a href="#scopeselector" title="ScopeSelector">ScopeSelector</a>" : <i>[ <a href="scopeselectordefinition.md">ScopeSelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hard" title="Hard">Hard</a>: <i>
      - <a href="harddefinition.md">HardDefinition</a></i>
<a href="#scopes" title="Scopes">Scopes</a>: <i>
      - String</i>
<a href="#scopeselector" title="ScopeSelector">ScopeSelector</a>: <i>
      - <a href="scopeselectordefinition.md">ScopeSelectorDefinition</a></i>
</pre>

## Properties

#### Hard

_Required_: No

_Type_: List of <a href="harddefinition.md">HardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeSelector

_Required_: No

_Type_: List of <a href="scopeselectordefinition.md">ScopeSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

