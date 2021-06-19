# TF::Intersight::WorkflowWorkflowInfo

Contains information for a workflow execution which is a runtime instance of workflow.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::WorkflowWorkflowInfo",
    "Properties" : {
        "<a href="#account" title="Account">Account</a>" : <i>[ <a href="accountdefinition.md">AccountDefinition</a>, ... ]</i>,
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#associatedobject" title="AssociatedObject">AssociatedObject</a>" : <i>[ <a href="associatedobjectdefinition.md">AssociatedObjectDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#cleanuptime" title="CleanupTime">CleanupTime</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
        "<a href="#failedworkflowcleanupduration" title="FailedWorkflowCleanupDuration">FailedWorkflowCleanupDuration</a>" : <i>Double</i>,
        "<a href="#input" title="Input">Input</a>" : <i>[ <a href="inputdefinition.md">InputDefinition</a>, ... ]</i>,
        "<a href="#instid" title="InstId">InstId</a>" : <i>String</i>,
        "<a href="#internal" title="Internal">Internal</a>" : <i>Boolean</i>,
        "<a href="#lastaction" title="LastAction">LastAction</a>" : <i>String</i>,
        "<a href="#message" title="Message">Message</a>" : <i>[ <a href="messagedefinition.md">MessageDefinition</a>, ... ]</i>,
        "<a href="#metaversion" title="MetaVersion">MetaVersion</a>" : <i>Double</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>[ <a href="organizationdefinition.md">OrganizationDefinition</a>, ... ]</i>,
        "<a href="#output" title="Output">Output</a>" : <i>[ <a href="outputdefinition.md">OutputDefinition</a>, ... ]</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#parenttaskinfo" title="ParentTaskInfo">ParentTaskInfo</a>" : <i>[ <a href="parenttaskinfodefinition.md">ParentTaskInfoDefinition</a>, ... ]</i>,
        "<a href="#pausereason" title="PauseReason">PauseReason</a>" : <i>String</i>,
        "<a href="#pendingdynamicworkflowinfo" title="PendingDynamicWorkflowInfo">PendingDynamicWorkflowInfo</a>" : <i>[ <a href="pendingdynamicworkflowinfodefinition.md">PendingDynamicWorkflowInfoDefinition</a>, ... ]</i>,
        "<a href="#permission" title="Permission">Permission</a>" : <i>[ <a href="permissiondefinition.md">PermissionDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#progress" title="Progress">Progress</a>" : <i>Double</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
        "<a href="#retryfromtaskname" title="RetryFromTaskName">RetryFromTaskName</a>" : <i>String</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#src" title="Src">Src</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#successworkflowcleanupduration" title="SuccessWorkflowCleanupDuration">SuccessWorkflowCleanupDuration</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#taskinfos" title="TaskInfos">TaskInfos</a>" : <i>[ <a href="taskinfosdefinition.md">TaskInfosDefinition</a>, ... ]</i>,
        "<a href="#traceid" title="TraceId">TraceId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#useractionrequired" title="UserActionRequired">UserActionRequired</a>" : <i>Boolean</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#waitreason" title="WaitReason">WaitReason</a>" : <i>String</i>,
        "<a href="#workflowctx" title="WorkflowCtx">WorkflowCtx</a>" : <i>[ <a href="workflowctxdefinition3.md">WorkflowCtxDefinition3</a>, ... ]</i>,
        "<a href="#workflowdefinition" title="WorkflowDefinition">WorkflowDefinition</a>" : <i>[ <a href="workflowdefinitiondefinition.md">WorkflowDefinitionDefinition</a>, ... ]</i>,
        "<a href="#workflowmetatype" title="WorkflowMetaType">WorkflowMetaType</a>" : <i>String</i>,
        "<a href="#workflowtaskcount" title="WorkflowTaskCount">WorkflowTaskCount</a>" : <i>Double</i>,
        "<a href="#workflowworkertaskcount" title="WorkflowWorkerTaskCount">WorkflowWorkerTaskCount</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::WorkflowWorkflowInfo
Properties:
    <a href="#account" title="Account">Account</a>: <i>
      - <a href="accountdefinition.md">AccountDefinition</a></i>
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#associatedobject" title="AssociatedObject">AssociatedObject</a>: <i>
      - <a href="associatedobjectdefinition.md">AssociatedObjectDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#cleanuptime" title="CleanupTime">CleanupTime</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
    <a href="#failedworkflowcleanupduration" title="FailedWorkflowCleanupDuration">FailedWorkflowCleanupDuration</a>: <i>Double</i>
    <a href="#input" title="Input">Input</a>: <i>
      - <a href="inputdefinition.md">InputDefinition</a></i>
    <a href="#instid" title="InstId">InstId</a>: <i>String</i>
    <a href="#internal" title="Internal">Internal</a>: <i>Boolean</i>
    <a href="#lastaction" title="LastAction">LastAction</a>: <i>String</i>
    <a href="#message" title="Message">Message</a>: <i>
      - <a href="messagedefinition.md">MessageDefinition</a></i>
    <a href="#metaversion" title="MetaVersion">MetaVersion</a>: <i>Double</i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>
      - <a href="organizationdefinition.md">OrganizationDefinition</a></i>
    <a href="#output" title="Output">Output</a>: <i>
      - <a href="outputdefinition.md">OutputDefinition</a></i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#parenttaskinfo" title="ParentTaskInfo">ParentTaskInfo</a>: <i>
      - <a href="parenttaskinfodefinition.md">ParentTaskInfoDefinition</a></i>
    <a href="#pausereason" title="PauseReason">PauseReason</a>: <i>String</i>
    <a href="#pendingdynamicworkflowinfo" title="PendingDynamicWorkflowInfo">PendingDynamicWorkflowInfo</a>: <i>
      - <a href="pendingdynamicworkflowinfodefinition.md">PendingDynamicWorkflowInfoDefinition</a></i>
    <a href="#permission" title="Permission">Permission</a>: <i>
      - <a href="permissiondefinition.md">PermissionDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#progress" title="Progress">Progress</a>: <i>Double</i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
    <a href="#retryfromtaskname" title="RetryFromTaskName">RetryFromTaskName</a>: <i>String</i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#src" title="Src">Src</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#successworkflowcleanupduration" title="SuccessWorkflowCleanupDuration">SuccessWorkflowCleanupDuration</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#taskinfos" title="TaskInfos">TaskInfos</a>: <i>
      - <a href="taskinfosdefinition.md">TaskInfosDefinition</a></i>
    <a href="#traceid" title="TraceId">TraceId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#useractionrequired" title="UserActionRequired">UserActionRequired</a>: <i>Boolean</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#waitreason" title="WaitReason">WaitReason</a>: <i>String</i>
    <a href="#workflowctx" title="WorkflowCtx">WorkflowCtx</a>: <i>
      - <a href="workflowctxdefinition3.md">WorkflowCtxDefinition3</a></i>
    <a href="#workflowdefinition" title="WorkflowDefinition">WorkflowDefinition</a>: <i>
      - <a href="workflowdefinitiondefinition.md">WorkflowDefinitionDefinition</a></i>
    <a href="#workflowmetatype" title="WorkflowMetaType">WorkflowMetaType</a>: <i>String</i>
    <a href="#workflowtaskcount" title="WorkflowTaskCount">WorkflowTaskCount</a>: <i>Double</i>
    <a href="#workflowworkertaskcount" title="WorkflowWorkerTaskCount">WorkflowWorkerTaskCount</a>: <i>Double</i>
</pre>

## Properties

#### Account

_Required_: No

_Type_: List of <a href="accountdefinition.md">AccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedObject

_Required_: No

_Type_: List of <a href="associatedobjectdefinition.md">AssociatedObjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleanupTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedWorkflowCleanupDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Input

_Required_: No

_Type_: List of <a href="inputdefinition.md">InputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: List of <a href="messagedefinition.md">MessageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: List of <a href="organizationdefinition.md">OrganizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Output

_Required_: No

_Type_: List of <a href="outputdefinition.md">OutputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: List of <a href="parentdefinition.md">ParentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentTaskInfo

_Required_: No

_Type_: List of <a href="parenttaskinfodefinition.md">ParentTaskInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PauseReason

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingDynamicWorkflowInfo

_Required_: No

_Type_: List of <a href="pendingdynamicworkflowinfodefinition.md">PendingDynamicWorkflowInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permission

_Required_: No

_Type_: List of <a href="permissiondefinition.md">PermissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionResources

_Required_: No

_Type_: List of <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Progress

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryFromTaskName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Src

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessWorkflowCleanupDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskInfos

_Required_: No

_Type_: List of <a href="taskinfosdefinition.md">TaskInfosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserActionRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitReason

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkflowCtx

_Required_: No

_Type_: List of <a href="workflowctxdefinition3.md">WorkflowCtxDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkflowDefinition

_Required_: No

_Type_: List of <a href="workflowdefinitiondefinition.md">WorkflowDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkflowMetaType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkflowTaskCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkflowWorkerTaskCount

_Required_: No

_Type_: Double

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

