# Terraform::Circonus::Check Jmx

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#mbeandomains" title="MbeanDomains">MbeanDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#mbeanproperties" title="MbeanProperties">MbeanProperties</a>" : <i>[ <a href="jmx-mbeanproperties.md">MbeanProperties</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#mbeandomains" title="MbeanDomains">MbeanDomains</a>: <i>
      - String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#mbeanproperties" title="MbeanProperties">MbeanProperties</a>: <i>
      - <a href="jmx-mbeanproperties.md">MbeanProperties</a></i>
</pre>

## Properties

#### Host

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MbeanDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MbeanProperties

_Required_: No

_Type_: List of <a href="jmx-mbeanproperties.md">MbeanProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

