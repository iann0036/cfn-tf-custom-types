# TF::AWS::AppmeshVirtualGateway SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backenddefaults" title="BackendDefaults">BackendDefaults</a>" : <i>[ <a href="backenddefaultsdefinition.md">BackendDefaultsDefinition</a>, ... ]</i>,
    "<a href="#listener" title="Listener">Listener</a>" : <i>[ <a href="listenerdefinition.md">ListenerDefinition</a>, ... ]</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="loggingdefinition.md">LoggingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backenddefaults" title="BackendDefaults">BackendDefaults</a>: <i>
      - <a href="backenddefaultsdefinition.md">BackendDefaultsDefinition</a></i>
<a href="#listener" title="Listener">Listener</a>: <i>
      - <a href="listenerdefinition.md">ListenerDefinition</a></i>
<a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="loggingdefinition.md">LoggingDefinition</a></i>
</pre>

## Properties

#### BackendDefaults

_Required_: No

_Type_: List of <a href="backenddefaultsdefinition.md">BackendDefaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No

_Type_: List of <a href="listenerdefinition.md">ListenerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="loggingdefinition.md">LoggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

