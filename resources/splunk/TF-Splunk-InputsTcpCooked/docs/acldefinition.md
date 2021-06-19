# TF::Splunk::InputsTcpCooked AclDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#app" title="App">App</a>" : <i>String</i>,
    "<a href="#canchangeperms" title="CanChangePerms">CanChangePerms</a>" : <i>Boolean</i>,
    "<a href="#canshareapp" title="CanShareApp">CanShareApp</a>" : <i>Boolean</i>,
    "<a href="#canshareglobal" title="CanShareGlobal">CanShareGlobal</a>" : <i>Boolean</i>,
    "<a href="#canshareuser" title="CanShareUser">CanShareUser</a>" : <i>Boolean</i>,
    "<a href="#canwrite" title="CanWrite">CanWrite</a>" : <i>Boolean</i>,
    "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
    "<a href="#read" title="Read">Read</a>" : <i>[ String, ... ]</i>,
    "<a href="#removable" title="Removable">Removable</a>" : <i>Boolean</i>,
    "<a href="#sharing" title="Sharing">Sharing</a>" : <i>String</i>,
    "<a href="#write" title="Write">Write</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#app" title="App">App</a>: <i>String</i>
<a href="#canchangeperms" title="CanChangePerms">CanChangePerms</a>: <i>Boolean</i>
<a href="#canshareapp" title="CanShareApp">CanShareApp</a>: <i>Boolean</i>
<a href="#canshareglobal" title="CanShareGlobal">CanShareGlobal</a>: <i>Boolean</i>
<a href="#canshareuser" title="CanShareUser">CanShareUser</a>: <i>Boolean</i>
<a href="#canwrite" title="CanWrite">CanWrite</a>: <i>Boolean</i>
<a href="#owner" title="Owner">Owner</a>: <i>String</i>
<a href="#read" title="Read">Read</a>: <i>
      - String</i>
<a href="#removable" title="Removable">Removable</a>: <i>Boolean</i>
<a href="#sharing" title="Sharing">Sharing</a>: <i>String</i>
<a href="#write" title="Write">Write</a>: <i>
      - String</i>
</pre>

## Properties

#### App

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanChangePerms

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanShareApp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanShareGlobal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanShareUser

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanWrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Read

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Removable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sharing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Write

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

